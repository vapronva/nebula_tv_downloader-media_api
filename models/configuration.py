from pydantic import BaseModel
from pathlib import Path


class ConfigurationNebulaAPIModel(BaseModel):
    USER_API_TOKEN: str
    AUTHORIZATION_HEADER: str | None = None
    USER_AGENT: str

    def __init__(self, **data):
        super().__init__(**data)
        self.AUTHORIZATION_HEADER = self.AUTHORIZATION_HEADER or None
        self.USER_AGENT = (
            self.USER_AGENT
            or "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
        )


class ConfigurationNebulaFiltersModel(BaseModel):
    CATEGORY_SEARCH: bool | str
    INCLUDE_NEBULA_FIRST: bool = True
    INCLUDE_NEBULA_PLUS: bool = True
    INCLUDE_REGULAR_VIDEOS: bool = False
    CHANNELS_TO_PARSE: list[str] | None = None


class ConfigurationDownloaderModel(BaseModel):
    DOWNLOAD_PATH: Path

    def __init__(self, **data):
        super().__init__(**data)
        self.DOWNLOAD_PATH = Path(self.DOWNLOAD_PATH)


class ConfigurationModel(BaseModel):
    NebulaAPI: ConfigurationNebulaAPIModel
    NebulaFilters: ConfigurationNebulaFiltersModel
    Downloader: ConfigurationDownloaderModel
