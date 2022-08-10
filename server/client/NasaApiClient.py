from datetime import datetime
from http import HTTPStatus
from typing import Optional

import requests

from server.model.ApodResponse import ApodResponse
from server.util.CustomLogger import CustomLogger
from server.util.EnvironmentReader import EnvironmentReader


class NasaApiClient:
    """
    https://api.nasa.gov/
    """

    def __init__(self):
        self.__LOGGER = CustomLogger.getLogger()
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

    def getApod(self) -> Optional[ApodResponse]:
        url = f"{self.__BASE_URL}{self.__APOD_ROUTE}?api_key={self.__API_KEY}"
        apod = None
        try:
            response = requests.get(url)
            response.raise_for_status()
            apod = self.__objectifyApodResponse(response.json())
        except Exception as e:
            self.__LOGGER.error(str(e))
        return apod
