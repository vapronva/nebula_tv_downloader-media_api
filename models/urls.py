from pydantic import HttpUrl, parse_obj_as


NEBULA_API_CONTENT_ALL_VIDEOS = parse_obj_as(
    HttpUrl, "https://content.api.nebula.app/video/{CATEGORY_QUERY}"
)

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

HTTP_API_CLASS_SLUG_INFORMATION = parse_obj_as(
    HttpUrl, "https://content.api.nebula.app/slug/{CLASS_SLUG}/{CLASS_NUMBER}/"
)
NEBULA_API_CLASS_STREAM_INFORMATION = parse_obj_as(
    HttpUrl,
    "https://content.api.nebula.app/class/{CLASS_SLUG}/lesson/{CLASS_NUMBER}/stream/",
)

NEBULA_USERAPI_AUTHORIZATION = parse_obj_as(
    HttpUrl, "https://users.api.nebula.app/api/v1/authorization/"
)
