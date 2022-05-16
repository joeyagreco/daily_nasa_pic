import tweepy
from tweepy import Client

from server.auth.TwitterAuth import TwitterAuth


class TwitterClient:
    __BEARER_TOKEN = TwitterAuth.BEARER_TOKEN
    __API_KEY = TwitterAuth.API_KEY
    __API_KEY_SECRET = TwitterAuth.API_KEY_SECRET
    __ACCESS_TOKEN = TwitterAuth.ACCESS_TOKEN
    __ACCESS_TOKEN_SECRET = TwitterAuth.ACCESS_TOKEN_SECRET

    @classmethod
    def getClient(cls) -> Client:
        return tweepy.Client(bearer_token=cls.__BEARER_TOKEN,
                             consumer_key=cls.__API_KEY,
                             consumer_secret=cls.__API_KEY_SECRET,
                             access_token=cls.__ACCESS_TOKEN,
                             access_token_secret=cls.__ACCESS_TOKEN_SECRET)
