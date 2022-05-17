import os

import requests


class ImageDownloader:

    @staticmethod
    def downloadImageByUrl(url: str, fileName: str, pathToSaveTo: str = None):
        fullPath = os.path.join(pathToSaveTo, fileName)
        response = requests.get(url)
        with open(fullPath, "wb") as f:
            f.write(response.content)
