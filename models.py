from typing import List, Optional
from pydantic import BaseModel, HttpUrl, NonNegativeInt


class NebulaChannelVideoContentDetailsAssets(BaseModel):
    avatar: Optional[dict]
    banner: Optional[dict]
    hero: Optional[dict]
    featured: Optional[dict]


class NebulaChannelVideoContentDetailsCategory(BaseModel):
    id: str
    type: str
    slug: str
    title: str
    assets: dict
    images: dict


class NebulaChannelVideoContentDetailsPlaylist(BaseModel):
    id: str
    type: str
    slug: str
    title: str


class NebulaChannelVideoContentDetails(BaseModel):
    id: str
    type: str
    slug: str
    title: str
    published_at: str
    description: Optional[str]
    assets: NebulaChannelVideoContentDetailsAssets
    images: dict
    genre_category_title: str
    genre_category_slug: str
    categories: List[NebulaChannelVideoContentDetailsCategory]
    website: Optional[HttpUrl]
    patreon: Optional[HttpUrl]
    twitter: Optional[HttpUrl]
    instagram: Optional[HttpUrl]
    facebook: Optional[HttpUrl]
    merch: Optional[HttpUrl]
    merch_collection: Optional[str]
    engagement: Optional[dict]
    playlists: List[NebulaChannelVideoContentDetailsPlaylist]
    zype_id: Optional[str]


class NebulaChannelVideoContentEpisodeResultAssets(BaseModel):
    channel_avatar: dict
    thumbnail: dict


class NebulaChannelVideoContentEpisodeResultImageInformation(BaseModel):
    formats: List[str]
    width: int
    height: int
    src: HttpUrl


class NebulaChannelVideoContentEpisodeResultImages(BaseModel):
    channel_avatar: NebulaChannelVideoContentEpisodeResultImageInformation
    thumbnail: NebulaChannelVideoContentEpisodeResultImageInformation


class NebulaChannelVideoContentEpisodeResult(BaseModel):
    id: str
    type: str
    slug: str
    title: str
    description: Optional[str]
    short_description: Optional[str]
    duration: NonNegativeInt
    duration_to_complete: NonNegativeInt
    published_at: str
    episode_url: Optional[HttpUrl]
    channel_id: str
    channel_slug: str
    channel_slugs: List[str]
    channel_title: str
    category_slugs: List[str]
    assets: NebulaChannelVideoContentEpisodeResultAssets
    images: NebulaChannelVideoContentEpisodeResultImages
    attributes: Optional[list]
    share_url: str
    channel: Optional[HttpUrl]
    engagement: Optional[dict]
    zype_id: str


class NebulaChannelVideoContentEpisodes(BaseModel):
    next: Optional[HttpUrl]
    previous: Optional[HttpUrl]
    results: List[NebulaChannelVideoContentEpisodeResult]


class NebulaChannelVideoContentResponseModel(BaseModel):
    details: NebulaChannelVideoContentDetails
    episodes: NebulaChannelVideoContentEpisodes


class NebulaUserAPIAuthorizationTokenResponseModel(BaseModel):
    token: str


class NebulaVideoContentStreamSubtitles(BaseModel):
    language_code: str
    url: HttpUrl
    language: str


class NebulaVideoContentStreamingResponseModel(BaseModel):
    manifest: HttpUrl
    download: HttpUrl
    iframe: HttpUrl
    bif: dict
    subtitles: List[NebulaVideoContentStreamSubtitles]
