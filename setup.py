from setuptools import setup, find_packages

setup(
    name="tweet_fetcher",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="DobleV55",
    author_email="vilavalentin@gmail.com",
    description="Python library to retrieve tweet data without consuming the API or using your X account.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DobleV55/tweet_fetcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
