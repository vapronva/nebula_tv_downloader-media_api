from pydantic import BaseModel, HttpUrl, NonNegativeInt


class NebulaChannelVideoContentDetailsAssets(BaseModel):
    avatar: dict | None
    banner: dict | None
    hero: dict | None
    featured: dict | None


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
    description: str | None
    assets: NebulaChannelVideoContentDetailsAssets
    images: dict
    genre_category_title: str
    genre_category_slug: str
    categories: list[NebulaChannelVideoContentDetailsCategory]
    website: HttpUrl | None
    patreon: HttpUrl | None
    twitter: HttpUrl | None
    instagram: HttpUrl | None
    facebook: HttpUrl | None
    merch: HttpUrl | None
    merch_collection: str | None
    engagement: dict | None
    playlists: list[NebulaChannelVideoContentDetailsPlaylist]
    zype_id: str | None
