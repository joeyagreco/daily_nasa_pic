import os
import time
from datetime import datetime

from server.client.NasaApiClient import NasaApiClient
from server.twitter.TwitterTweeter import TwitterTweeter
from server.util.CustomLogger import CustomLogger
from server.util.ImageDownloader import ImageDownloader


class BotRunner:

    def __init__(self):
        self.__LOGGER = CustomLogger.getLogger()
        self.__SLEEP_FOR_SECONDS = 50

    def run(self, hourToRunAt: int):
        nasaApiClient = NasaApiClient()
        while True:
            # run this daily at the top of the given hour (in military time)
            # Example:
            #   12 -> run at 12:00PM
            #   20 -> run at 8:00PM
            #   6 -> run at 6:00AM
            now = datetime.now()
            if now.hour == hourToRunAt and now.minute == 0:
                self.__LOGGER.info(f"TIME MATCH... RUNNING BOT...")
                # get Astronomy Picture of the Day
                apod = nasaApiClient.getApod()
                tmpFolderDirectory = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../tmp"))
                fileName = "tmp.jpg"
                # delete old image from tmp folder if there is one
                fullImagePath = os.path.join(tmpFolderDirectory, fileName)
                if os.path.exists(fullImagePath):
                    os.remove(fullImagePath)
                # download image locally to tmp folder
                ImageDownloader.downloadImageByUrl(apod.url, fileName, tmpFolderDirectory)
                # create and send tweet
                twitterTweeter = TwitterTweeter()
                tweetText = f'"{apod.title}"\n\n{apod.copyright}'
                twitterTweeter.createTweet(tweetText, mediaUrls=[fullImagePath])
            # sleep until next check
            self.__LOGGER.info(f"SLEEPING FOR {self.__SLEEP_FOR_SECONDS} SECONDS...")
            time.sleep(self.__SLEEP_FOR_SECONDS)


