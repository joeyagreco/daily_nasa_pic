from typing import List

from tweepy.models import Status

from server.twitter.TwitterAPI import TwitterAPI


class TwitterSearcher:

    @classmethod
    def getLatestTweetsByUsername(cls, userId: int, count: int = 1) -> List[Status]:
        api = TwitterAPI.getAPI()
        return api.user_timeline(user_id=userId, count=count)
