# Daily NASA Pic

Daily NASA Pic is a Twitter bot that uses the [NASA API](https://api.nasa.gov/) to tweet out the image daily.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Setup

The following environment variables must be defined before running the script:

```dotenv
# TWITTER

TWITTER_API_KEY=...
TWITTER_API_KEY_SECRET=...
TWITTER_BEARER_TOKEN=...
TWITTER_ACCESS_TOKEN=...
TWITTER_ACCESS_TOKEN_SECRET=...
TWEET_BASE_URL=https://twitter.com/{account_@_name}/status/
TWITTER_ACCOUNT_ID=...

# NASA API

NASA_API_BASE_URL=https://api.nasa.gov/planetary
NASA_API_APOD_ROUTE=/apod
NASA_API_KEY=...

# GENERAL

# uses military time (1-24)
HOUR_TO_RUN_BOT_AT=12
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
