from pydantic import BaseModel, HttpUrl


class NebulaVideoContentStreamSubtitles(BaseModel):
    language_code: str
    url: HttpUrl
    language: str


class NebulaVideoContentStreamingResponseModel(BaseModel):
    manifest: HttpUrl
    download: HttpUrl | str | None
    iframe: HttpUrl | None
    bif: dict
    subtitles: list[NebulaVideoContentStreamSubtitles]
