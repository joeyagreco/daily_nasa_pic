import os

import requests

from server.util.CustomLogger import CustomLogger


class ImageDownloader:
    __LOGGER = CustomLogger.getLogger()

    @classmethod
    def downloadImageByUrl(cls, url: str, fileName: str, pathToSaveTo: str = None):
        try:
            fullPath = os.path.join(pathToSaveTo, fileName)
            response = requests.get(url)
            response.raise_for_status()
            with open(fullPath, "wb") as f:
                f.write(response.content)
        except Exception as e:
            cls.__LOGGER.error(str(e))
            raise e
