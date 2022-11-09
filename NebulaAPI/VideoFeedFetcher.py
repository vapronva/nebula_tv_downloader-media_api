from requests import get as requests_get
import logging
from models.urls import NEBULA_API_CONTENT_ALL_VIDEOS
from models.nebula.Fetched import (
    NebulaChannelVideoContentEpisodes,
    NebulaChannelVideoContentEpisodeResult,
)


def get_all_channels_slugs_from_video_feed(
    authorizationHeader: str,
    categoryFeedSelector: str | None = None,
    cursorTimesLimitFetchMaximum: int = 100,
) -> list[str]:
    response = requests_get(
        url=NEBULA_API_CONTENT_ALL_VIDEOS.format(
            CATEGORY_QUERY=f"?category={categoryFeedSelector}"
            if categoryFeedSelector is not None
            else ""
        ),
        headers={"Authorization": authorizationHeader},
    )
    if response.status_code == 200:
        data = NebulaChannelVideoContentEpisodes(**response.json())
        logging.info(
            "Received %s episodes from the initial video feed request",
            len(data.results),
        )
        cursorTimes = 0
        while data.next is not None and cursorTimes < cursorTimesLimitFetchMaximum:
            response = requests_get(
                url=data.next,
                headers={
                    "Authorization": authorizationHeader,
                },
            )
            if response.status_code == 200:
                cursoredData = NebulaChannelVideoContentEpisodes(**response.json())
                logging.info(
                    "Received %s episodes from the video feed for page #%s (total episodes: %s)",
                    len(cursoredData.results),
                    cursorTimes,
                    len(data.results),
                )
                data.results.extend(cursoredData.results)
                data.next = cursoredData.next
                cursorTimes += 1
                continue
            raise Exception(
                f"Failed to get video feed for the page #{cursorTimes}: `{response.content}` with status code {response.status_code}"
            )
        channels = list({x.channel_slug for x in data.results})
        logging.info(
            "Found %s channels in video feed in the last %s pages with %s episodes%s",
            len(channels),
            cursorTimes,
            len(data.results),
            f" for category `{categoryFeedSelector}`"
            if categoryFeedSelector is not None
            else "",
        )
        logging.debug("Found channels: %s", channels)
        return (
            channels  # if not okShouldReturnAllEpisodesListActually else data.results
        )
    raise Exception(
        f"Failed to get video feed: `{response.content[:30]}...` with status code {response.status_code}"
    )
