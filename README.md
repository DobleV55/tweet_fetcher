# tweet_fetcher

tweet_fetcher is a Python library to retrieve tweet data without consuming the API or using your X account.

## Installation

You can install the package using pip:

```bash
pip install tweet_fetcher
```

## Usage

Here's an example of how to use the library:

```python
from tweet_fetcher import get_tweet_data

tweet_data = get_tweet_data("1465392570310217728")
print(tweet_data)
```

### Methods

- get_tweet_data(tweet_id_or_url)
  Retrieve tweet data given its ID (int or str) or URL.

### Parameters:

- tweet_id_or_url (str): The tweet ID (as int or str) or URL.

### Returns:

- dict: The tweet data in JSON format.

### Example:

```python
from tweet_fetcher import get_tweet_data

tweet_data = get_tweet_data("https://x.com/valen_vila00/status/1465392570310217728")
print(tweet_data)
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Me.
