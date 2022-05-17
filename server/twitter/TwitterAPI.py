import tweepy
from tweepy import Client, API, OAuthHandler

from server.auth.TwitterAuth import TwitterAuth


class TwitterAPI:
    __BEARER_TOKEN = TwitterAuth.BEARER_TOKEN
    __API_KEY = TwitterAuth.API_KEY
    __API_KEY_SECRET = TwitterAuth.API_KEY_SECRET
    __ACCESS_TOKEN = TwitterAuth.ACCESS_TOKEN
    __ACCESS_TOKEN_SECRET = TwitterAuth.ACCESS_TOKEN_SECRET

    @classmethod
    def __getOAuthHandler(cls) -> OAuthHandler:
        handler = tweepy.OAuthHandler(cls.__API_KEY, cls.__API_KEY_SECRET)
        handler.set_access_token(cls.__ACCESS_TOKEN, cls.__ACCESS_TOKEN_SECRET)
        return handler

    @classmethod
    def getAPI(cls) -> API:
        return tweepy.API(cls.__getOAuthHandler())
