import os
import time
from datetime import datetime

from server.client.NasaApiClient import NasaApiClient
from server.twitter.TwitterTweeter import TwitterTweeter
from server.util.CustomLogger import CustomLogger
from server.util.EnvironmentReader import EnvironmentReader
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
            # if now.hour == hourToRunAt and now.minute == 0:
            if True:
                self.__LOGGER.info(f"TIME MATCH... RUNNING BOT...")
                # get Astronomy Picture of the Day
                apod = nasaApiClient.getApod()
                tmpFolderDirectory = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../tmp"))
                fileName = "tmp.jpg"
                # create the tmp directory if it doesn't already exist
                if not os.path.exists(tmpFolderDirectory):
                    self.__LOGGER.info(f"CREATING DIRECTORY AT '{tmpFolderDirectory}'")
                    os.makedirs(tmpFolderDirectory)
                # delete old image from tmp folder if there is one
                fullImagePath = os.path.join(tmpFolderDirectory, fileName)
                if os.path.exists(fullImagePath):
                    os.remove(fullImagePath)
                # download image locally to tmp folder
                ImageDownloader.downloadImageByUrl(apod.url, fileName, tmpFolderDirectory)
                # create and send tweet
                twitterTweeter = TwitterTweeter()
                tweetText = f'{apod.date.strftime("%B %#d, %Y")}\n\n"{apod.title}"\n\n{apod.copyright}'
                status = twitterTweeter.createTweet(tweetText, mediaUrls=[fullImagePath])
                self.__LOGGER.info(f"TWEETED SUCCESSFULLY: {EnvironmentReader.get('TWEET_BASE_URL')}{status.id}")
            # sleep until next check
            self.__LOGGER.info(f"SLEEPING FOR {self.__SLEEP_FOR_SECONDS} SECONDS...")
            time.sleep(self.__SLEEP_FOR_SECONDS)


