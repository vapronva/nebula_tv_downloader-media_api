from pathlib import Path
from typing import List, Optional
from pydantic import HttpUrl, parse_obj_as


NEBULA_API_CONTENT_VIDEO_CHANNELS = parse_obj_as(
    HttpUrl, "https://content.api.nebula.app/video/channels/{CHANNEL_SLUG}/"
)
NEBULA_API_CONTENT_VIDEO_CHANNELS_CURSOR = parse_obj_as(
    HttpUrl,
    "https://content.api.nebula.app/video/channels/{CHANNEL_SLUG}/?cursor={CURSOR}",
)

NEBULA_API_VIDEO_STREAM_INFORMATION = parse_obj_as(
    HttpUrl, "https://content.api.nebula.app/video/{VIDEO_SLUG}/stream/"
)

NEBULA_USERAPI_AUTHORIZATION = parse_obj_as(
    HttpUrl, "https://users.api.nebula.app/api/v1/authorization/"
)

TOKEN_NEBULA_USERAPI_AUTHORIZATION: str = ""
TOKEN_NEBULA_FINAL_AUTHORIZATION: Optional[str] = ""

PARSE_NEBULA_CHANNLES_SLUGS: List[str] = []

VIDEOS_OUTPUT_DIRECTORY: Path = Path("./")
