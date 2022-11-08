from configparser import ConfigParser
from models.configuration import *


class Config:
    def __init__(self) -> None:
        configOriginal = ConfigParser()
        configOriginal.read("config.example.ini")
        self.__CONFIG = ConfigurationModel(
            NebulaAPI=ConfigurationNebulaAPIModel(
                USER_API_TOKEN=configOriginal["NebulaAPI"]["USER_API_TOKEN"],
                AUTHORIZATION_HEADER=configOriginal["NebulaAPI"][
                    "AUTHORIZATION_HEADER"
                ],
            ),
            NebulaFilters=ConfigurationNebulaFiltersModel(
                CATEGORY_SEARCH=str(configOriginal["NebulaFilters"]["CATEGORY_SEARCH"]),
                INCLUDE_NEBULA_FIRST=bool(
                    configOriginal["NebulaFilters"]["INCLUDE_NEBULA_FIRST"]
                ),
                INCLUDE_NEBULA_PLUS=bool(
                    configOriginal["NebulaFilters"]["INCLUDE_NEBULA_PLUS"]
                ),
                INCLUDE_REGULAR_VIDEOS=bool(
                    configOriginal["NebulaFilters"]["INCLUDE_REGULAR_VIDEOS"]
                ),
                CHANNELS_TO_PARSE=configOriginal["NebulaFilters"][
                    "CHANNELS_TO_PARSE"
                ].split(",")
                if configOriginal["NebulaFilters"]["CHANNELS_TO_PARSE"]
                else None,
            ),
            Downloader=ConfigurationDownloaderModel(
                DOWNLOAD_PATH=configOriginal["Downloader"]["DOWNLOAD_PATH"],
            ),
        )

    @property
    def NebulaAPI(self) -> ConfigurationNebulaAPIModel:
        return self.__CONFIG.NebulaAPI

    @property
    def NebulaFilters(self) -> ConfigurationNebulaFiltersModel:
        return self.__CONFIG.NebulaFilters

    @property
    def Downloader(self) -> ConfigurationDownloaderModel:
        return self.__CONFIG.Downloader

    def setNebulaAuthorizationToken(self, token: str) -> None:
        self.__CONFIG.NebulaAPI.AUTHORIZATION_HEADER = token
