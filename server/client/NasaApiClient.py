from datetime import datetime
from typing import Optional

import requests

from server.model.ApodResponse import ApodResponse
from server.util.EnvironmentReader import EnvironmentReader


class NasaApiClient:
    """
    https://api.nasa.gov/
    """

    def __init__(self):
        self.__BASE_URL = EnvironmentReader.get("NASA_API_BASE_URL")
        self.__APOD_ROUTE = EnvironmentReader.get("NASA_API_APOD_ROUTE")
        self.__API_KEY = EnvironmentReader.get("NASA_API_KEY")

    def __objectifyApodResponse(self, apodResponse: dict) -> Optional[ApodResponse]:
        apodResponseObj = None
        if apodResponse:
            apodResponseObj = ApodResponse(copyright=apodResponse.get("copyright", None),
                                           date=datetime.strptime(apodResponse["date"], "%Y-%m-%d"),
                                           explanation=apodResponse["explanation"],
                                           hdUrl=apodResponse["hdurl"],
                                           mediaType=apodResponse["media_type"],
                                           serviceVersion=apodResponse["service_version"],
                                           title=apodResponse["title"],
                                           url=apodResponse["url"])
        return apodResponseObj

    def getApod(self) -> ApodResponse:
        url = f"{self.__BASE_URL}{self.__APOD_ROUTE}?api_key={self.__API_KEY}"
        response = requests.get(url).json()
        return self.__objectifyApodResponse(response)

