import requests
import math


def _generate_token(tweet_id):
    """Generate a token based on the tweet ID."""
    token = (float(tweet_id) / 1e15) * math.pi
    base36_token = _base36_encode(token)
    cleaned_token = base36_token.replace('0', '').replace('.', '')
    return cleaned_token


def _base36_encode(number):
    """Convert a decimal number to a base-36 string."""
    if number == 0:
        return '0'
    base36 = ''
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    integer_part = int(number)
    fractional_part = number - integer_part

    # Convert the integer part
    if integer_part == 0:
        base36 = '0'
    while integer_part:
        integer_part, mod = divmod(integer_part, 36)
        base36 = alphabet[mod] + base36

    # Convert the fractional part
    if fractional_part > 0:
        base36 += '.'
        # Limit length to avoid infinite loops
        while fractional_part and len(base36) < 20:
            fractional_part *= 36
            digit = int(fractional_part)
            base36 += alphabet[digit]
            fractional_part -= digit

    return base36


def get_tweet_data(tweet_id_or_url):
    """Retrieve tweet data given its ID or URL."""
    if isinstance(tweet_id_or_url, str) and tweet_id_or_url.startswith("http"):
        # Extract tweet ID from URL
        tweet_id = tweet_id_or_url.split("/")[-1]
    else:
        # Assume input is the tweet ID
        tweet_id = str(tweet_id_or_url)

    token = _generate_token(tweet_id)
    url = f"https://cdn.syndication.twimg.com/tweet-result?id={tweet_id}&lang=en&token={token}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
