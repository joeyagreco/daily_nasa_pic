import os
import time
from datetime import datetime

from server.client.NasaApiClient import NasaApiClient
from server.model.ApodResponse import ApodResponse
from server.twitter.TwitterSearcher import TwitterSearcher
from server.twitter.TwitterTweeter import TwitterTweeter
from server.util.CustomLogger import CustomLogger
from server.util.EnvironmentReader import EnvironmentReader
from server.util.ImageDownloader import ImageDownloader


class BotRunner:

    def __init__(self):
        self.__LOGGER = CustomLogger.getLogger()
        self.__SECONDS_IN_MINUTE = 60
        self.__SLEEP_FOR_MINUTES = 50
        self.__GET_APOD_MAX_RETRIES = 5
        self.__GET_APOD_SLEEP_FOR_MINUTES = 2
        self.__DOWNLOAD_IMAGE_MAX_RETRIES = 5
        self.__DOWNLOAD_IMAGE_SLEEP_FOR_MINUTES = 2
        self.__TMP_DIRECTORY_NAME = "tmp"
        self.__TMP_FILE_NAME = "tmp.jpg"
        self.__TWITTER_ACCOUNT_ID = EnvironmentReader.get("TWITTER_ACCOUNT_ID", int)

    def run(self, hourToRunAt: int):
        nasaApiClient = NasaApiClient()
        while True:
            # run this daily at the given hour
            # Example:
            #   12 -> run after 12:00PM
            #   20 -> run after 8:00PM
            #   6 -> run after 6:00AM
            now = datetime.now()
            # get the latest tweet from the account to see if the account has already tweeted today
            latestTweetsList = TwitterSearcher.getLatestTweetsByUsername(self.__TWITTER_ACCOUNT_ID, count=1)
            if (now.hour == hourToRunAt and len(latestTweetsList) == 0) \
                    or latestTweetsList[0].created_at.day != now.day:
                self.__LOGGER.info(f"TIME MATCH... RUNNING BOT...")

                # get Astronomy Picture of the Day
                for _ in range(self.__GET_APOD_MAX_RETRIES):
                    apod = nasaApiClient.getApod()
                    if apod is not None:
                        break
                    self.__LOGGER.warning(f"COULD NOT GET APOD.")
                    self.__LOGGER.warning(
                        f"SLEEPING FOR {self.__GET_APOD_SLEEP_FOR_MINUTES * self.__SECONDS_IN_MINUTE} MINUTES...")
                    time.sleep(self.__GET_APOD_SLEEP_FOR_MINUTES * self.__SECONDS_IN_MINUTE)
                    continue

                tmpFolderDirectory = os.path.abspath(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"../{self.__TMP_DIRECTORY_NAME}"))
                fileName = self.__TMP_FILE_NAME
                # create the tmp directory if it doesn't already exist
                if not os.path.exists(tmpFolderDirectory):
                    self.__LOGGER.info(f"CREATING DIRECTORY AT '{tmpFolderDirectory}'")
                    os.makedirs(tmpFolderDirectory)
                # delete old image from tmp folder if there is one
                fullImagePath = os.path.join(tmpFolderDirectory, fileName)
                if os.path.exists(fullImagePath):
                    os.remove(fullImagePath)

                if apod.hdUrl is not None:
                    # we have an image for this APOD
                    for _ in range(self.__DOWNLOAD_IMAGE_MAX_RETRIES):
                        # download image locally to tmp folder
                        try:
                            ImageDownloader.downloadImageByUrl(apod.url, fileName, tmpFolderDirectory)
                        except Exception as e:
                            self.__LOGGER.warning(f"COULD NOT GET APOD.")
                            self.__LOGGER.warning(
                                f"SLEEPING FOR {self.__DOWNLOAD_IMAGE_SLEEP_FOR_MINUTES * self.__SECONDS_IN_MINUTE} MINUTES...")
                            time.sleep(self.__DOWNLOAD_IMAGE_SLEEP_FOR_MINUTES * self.__SECONDS_IN_MINUTE)

                # create and send tweet
                twitterTweeter = TwitterTweeter()
                tweetText = self.__buildTweet(apod)
                if apod.hdUrl:
                    # sending with image
                    status = twitterTweeter.createTweet(tweetText, mediaUrls=[fullImagePath])
                else:
                    # sending with link
                    status = twitterTweeter.createTweet(tweetText)
                self.__LOGGER.info(f"TWEETED SUCCESSFULLY: {EnvironmentReader.get('TWEET_BASE_URL')}{status.id}")

            # sleep until next check
            self.__LOGGER.info(f"SLEEPING FOR {self.__SLEEP_FOR_MINUTES} MINUTES...")
            time.sleep(self.__SLEEP_FOR_MINUTES * self.__SECONDS_IN_MINUTE)

    def __buildTweet(self, apod: ApodResponse) -> str:
        tweetStr = f'{apod.date.strftime("%B %#d, %Y")}\n\n"{apod.title}"'
        if apod.copyright:
            tweetStr += f"\n\n{apod.copyright}"
        if not apod.hdUrl and apod.url:
            tweetStr += f"\n\n{apod.url}"
        return tweetStr
