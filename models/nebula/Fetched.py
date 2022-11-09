from pydantic import BaseModel, HttpUrl
from Episode import NebulaChannelVideoContentEpisodeResult
from Channel import NebulaChannelVideoContentDetails


class NebulaChannelVideoContentEpisodes(BaseModel):
    next: HttpUrl | None
    previous: HttpUrl | None
    results: list[NebulaChannelVideoContentEpisodeResult]


class NebulaChannelVideoContentResponseModel(BaseModel):
    details: NebulaChannelVideoContentDetails
    episodes: NebulaChannelVideoContentEpisodes
