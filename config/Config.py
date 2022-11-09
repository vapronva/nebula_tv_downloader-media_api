from configparser import ConfigParser
from pathlib import Path
from models.configuration import (
    ConfigurationModel,
    ConfigurationNebulaAPIModel,
    ConfigurationNebulaFiltersModel,
    ConfigurationDownloaderModel,
)


class Config:
    def __init__(self, configPath: Path = Path("config/config.ini")) -> None:
        configOriginal = ConfigParser()
        configOriginal.read(configPath)
        self.__CONFIG = ConfigurationModel(
            NebulaAPI=ConfigurationNebulaAPIModel(
                USER_API_TOKEN=configOriginal["NebulaAPI"]["USER_API_TOKEN"],
                AUTHORIZATION_HEADER=configOriginal["NebulaAPI"][
                    "AUTHORIZATION_HEADER"
                ],
                USER_AGENT=configOriginal["NebulaAPI"]["USER_AGENT"]
                if configOriginal["NebulaAPI"]["USER_AGENT"]
                else None,
            ),
            NebulaFilters=ConfigurationNebulaFiltersModel(
                CATEGORY_SEARCH=str(configOriginal["NebulaFilters"]["CATEGORY_SEARCH"])
                if not configOriginal["NebulaFilters"]["CATEGORY_SEARCH"] == "false"
                else None,
                INCLUDE_NEBULA_FIRST=configOriginal.getboolean(
                    "NebulaFilters", "INCLUDE_NEBULA_FIRST"
                ),
                INCLUDE_NEBULA_PLUS=configOriginal.getboolean(
                    "NebulaFilters", "INCLUDE_NEBULA_PLUS"
                ),
                INCLUDE_NEBULA_ORIGINALS=configOriginal.getboolean(
                    "NebulaFilters", "INCLUDE_NEBULA_ORIGINALS"
                ),
                INCLUDE_REGULAR_VIDEOS=configOriginal.getboolean(
                    "NebulaFilters", "INCLUDE_REGULAR_VIDEOS"
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
