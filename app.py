import os

from server.client.NasaApiClient import NasaApiClient
from server.twitter.TwitterTweeter import TwitterTweeter
from server.util.ImageDownloader import ImageDownloader

if __name__ == "__main__":
    # filePath = "C:/Users/14143/PycharmProjects/daily_nasa_pic"
    # fileName = "tmp.jpg"
    # ImageDownloader.downloadImageByUrl("https://apod.nasa.gov/apod/image/2205/CoiffeesMW_Barakat_960.jpg", fileName, filePath)
    # tt = TwitterTweeter()
    # tt.createTweet("test jg", mediaUrls=[os.path.join(filePath, fileName)])
    nac = NasaApiClient()
    apod = nac.getApod()
    print(apod)
