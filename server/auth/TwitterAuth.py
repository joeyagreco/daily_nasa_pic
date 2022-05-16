from server.util.EnvironmentReader import EnvironmentReader


class TwitterAuth:
    API_KEY = EnvironmentReader.get("TWITTER_API_KEY")
    API_KEY_SECRET = EnvironmentReader.get("TWITTER_API_KEY_SECRET")
    BEARER_TOKEN = EnvironmentReader.get("TWITTER_BEARER_TOKEN")
    ACCESS_TOKEN = EnvironmentReader.get("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = EnvironmentReader.get("TWITTER_ACCESS_TOKEN_SECRET")
