from requests import get as requests_get
import logging
from time import sleep
from models.nebula.Fetched import NebulaChannelVideoContentResponseModel
from models.urls import NEBULA_API_CONTENT_VIDEO_CHANNELS


def get_channel_video_content(
    channelSlug: str, authorizationHeader: str, waitAfterUnsuccessfulSeconds: int = 5
) -> NebulaChannelVideoContentResponseModel:
    response = requests_get(
        url=NEBULA_API_CONTENT_VIDEO_CHANNELS.format(CHANNEL_SLUG=channelSlug),
        headers={
            "Authorization": authorizationHeader,
        },
    )
    if response.status_code == 200:
        currentData = NebulaChannelVideoContentResponseModel(**response.json())
        logging.info(
            "Received %s videos from channel `%s` in the initial request",
            len(currentData.episodes.results),
            channelSlug,
        )
        currentCursorTimes = 0
        while currentData.episodes.next is not None:
            response = requests_get(
                url=currentData.episodes.next,
                headers={
                    "Authorization": authorizationHeader,
                },
            )
            if response.status_code == 200:
                data = NebulaChannelVideoContentResponseModel(**response.json())
                logging.info(
                    "Received %s videos from channel `%s` from page #%s (total videos: %s)",
                    len(data.episodes.results),
                    channelSlug,
                    currentCursorTimes,
                    len(currentData.episodes.results),
                )
                currentData.episodes.results.extend(data.episodes.results)
                currentData.episodes.next = data.episodes.next
                currentCursorTimes += 1
                continue
            elif response.status_code == 404:
                logging.warning(
                    "Channel `%s` does not exist anymore",
                    channelSlug,
                )
                return currentData
            elif response.status_code == 429:
                logging.warning(
                    "Rate limit reached for channel `%s`, waiting %s seconds",
                    channelSlug,
                    waitAfterUnsuccessfulSeconds,
                )
                sleep(waitAfterUnsuccessfulSeconds)
                waitAfterUnsuccessfulSeconds *= 2
                continue
            raise Exception(
                f"Failed to get channel video content for page #{currentCursorTimes} for `{channelSlug}`: `{response.content}` with status code {response.status_code}"
            )
        return currentData
    raise Exception(
        f"Failed to get channel video content for `{channelSlug}`: `{response.content}` with status code {response.status_code}"
    )
