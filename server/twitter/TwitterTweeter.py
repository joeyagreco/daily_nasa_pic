from tweepy import Response

from server.twitter.TwitterAPI import TwitterAPI


class TwitterTweeter:

    @classmethod
    def createTweet(cls, text: str, **kwargs) -> Response:
        mediaUrls = kwargs.pop("mediaUrls", list())
        api = TwitterAPI.getAPI()
        medias = list()
        for url in mediaUrls:
            medias.append(api.media_upload(url))
        return api.update_status(status=text, media_ids=[m.media_id for m in medias])
