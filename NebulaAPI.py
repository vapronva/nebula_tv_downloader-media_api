from models import (
    NebulaChannelVideoContentResponseModel,
    NebulaUserAPIAuthorizationTokenResponseModel,
    NebulaVideoContentStreamingResponseModel,
    NebulaVideoContentStreamingResponseModel,
    NebulaChannelVideoContentEpisodes,
)
from config import *
import requests
import logging
from time import sleep

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

__TOKEN_NEBULA_FINAL_AUTHORIZATION = TOKEN_NEBULA_FINAL_AUTHORIZATION


def get_authorization_token(user_token: str) -> str:
    global __TOKEN_NEBULA_FINAL_AUTHORIZATION
    if __TOKEN_NEBULA_FINAL_AUTHORIZATION is None:
        response = requests.post(
            url=NEBULA_USERAPI_AUTHORIZATION,
            headers={
                "Authorization": f"Token {user_token}",
            },
        )
        if response.status_code == 200:
            data = NebulaUserAPIAuthorizationTokenResponseModel(**response.json())
            __TOKEN_NEBULA_FINAL_AUTHORIZATION = data.token
            logging.info(
                f"Successfully got Nebula authorization token: {__TOKEN_NEBULA_FINAL_AUTHORIZATION}"
            )
        raise Exception(
            f"Failed to get authorization token: {response.content} with status code {response.status_code}"
        )
    return __TOKEN_NEBULA_FINAL_AUTHORIZATION


def get_channel_video_content(
    channel_slug: str,
) -> NebulaChannelVideoContentResponseModel:
    response = requests.get(
        url=NEBULA_API_CONTENT_VIDEO_CHANNELS.format(CHANNEL_SLUG=channel_slug),
        headers={
            "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
        },
    )
    if response.status_code == 200:
        currentData = NebulaChannelVideoContentResponseModel(**response.json())
        logging.info(
            f"Received {len(currentData.episodes.results)} videos from channel `{channel_slug}`"
        )
        while currentData.episodes.next is not None:
            response = requests.get(
                url=currentData.episodes.next,
                headers={
                    "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
                },
            )
            if response.status_code == 200:
                data = NebulaChannelVideoContentResponseModel(**response.json())
                logging.info(
                    f"Received {len(data.episodes.results)} videos from channel `{channel_slug}` (next page) (total videos: {len(currentData.episodes.results)})"
                )
                currentData.episodes.results.extend(data.episodes.results)
                currentData.episodes.next = data.episodes.next
                continue
            raise Exception(
                f"Failed to get channel video content for next page for {channel_slug}: {response.content} with status code {response.status_code}"
            )
        return currentData
    raise Exception(
        f"Failed to get channel video content for {channel_slug}: {response.content} with status code {response.status_code}"
    )


def get_straming_info(video_slug: str) -> NebulaVideoContentStreamingResponseModel:
    response = requests.get(
        url=NEBULA_API_VIDEO_STREAM_INFORMATION.format(VIDEO_SLUG=video_slug),
        headers={
            "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
        },
    )
    if response.status_code == 200:
        return NebulaVideoContentStreamingResponseModel(**response.json())
    elif response.status_code == 403:
        logging.info("Got restricted ... Please buy another subscription.")
        sleep(5)
        return get_straming_info(video_slug)
    elif response.status_code == 429:
        logging.info(f"Thtrottled by Nebula API, waiting for 5 seconds...")
        sleep(5)
        return get_straming_info(video_slug)
    raise Exception(
        f"Failed to get video streaming info for {video_slug}: {response.content} with status code {response.status_code}"
    )


def get_all_channels_from_video_feed(cursorTimesLimit: int = 100) -> List[str]:
    response = requests.get(
        url=NEBULA_API_CONTENT_ALL_VIDEOS,
        headers={
            "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
        },
    )
    if response.status_code == 200:
        data = NebulaChannelVideoContentEpisodes(**response.json())
        logging.info(f"Received {len(data.results)} episodes from video feed")
        cursorTimes = 0
        while data.next is not None and cursorTimes < cursorTimesLimit:
            response = requests.get(
                url=data.next,
                headers={
                    "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
                },
            )
            if response.status_code == 200:
                cursoredData = NebulaChannelVideoContentEpisodes(**response.json())
                logging.info(
                    f"Received {len(cursoredData.results)} episodes from video feed (next page) (current page: {cursorTimes}; total episodes: {len(data.results)})"
                )
                data.results.extend(cursoredData.results)
                data.next = cursoredData.next
                cursorTimes += 1
                continue
            raise Exception(
                f"Failed to get video feed for next page: {response.content} with status code {response.status_code}"
            )
        channels = list(set([x.channel_slug for x in data.results]))
        logging.info(
            f"Found {len(channels)} channels in video feed in the last {cursorTimes} pages"
        )
        logging.debug(f"Channels: {channels}")
        return channels
    raise Exception(
        f"Failed to get video feed: {response.content} with status code {response.status_code}"
    )
