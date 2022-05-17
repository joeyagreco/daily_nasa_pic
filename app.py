from server.twitter.TwitterTweeter import TwitterTweeter
from server.util.ImageDownloader import ImageDownloader

if __name__ == "__main__":
    ImageDownloader.downloadImageByUrl("https://apod.nasa.gov/apod/image/2205/CoiffeesMW_Barakat_960.jpg", "tmp.jpg", "C:/Users/14143/PycharmProjects/daily_nasa_pic")
    # tt = TwitterTweeter()
    # tt.createTweet("test jg", mediaUrls=["img.png"])
