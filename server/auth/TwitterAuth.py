import tweepy

from server.util.EnvironmentReader import EnvironmentReader


class TwitterAuth:
    API_KEY = EnvironmentReader.get("TWITTER_API_KEY")
    API_KEY_SECRET = EnvironmentReader.get("TWITTER_API_KEY_SECRET")
    BEARER_TOKEN = EnvironmentReader.get("TWITTER_BEARER_TOKEN")
    ACCESS_TOKEN = EnvironmentReader.get("TWITTER_ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = EnvironmentReader.get("TWITTER_ACCESS_TOKEN_SECRET")

    @classmethod
    def getOAuthHandler(cls):
        handler = tweepy.OAuthHandler(cls.API_KEY, cls.API_KEY_SECRET)
        handler.set_access_token(cls.ACCESS_TOKEN, cls.ACCESS_TOKEN_SECRET)
        return handler
