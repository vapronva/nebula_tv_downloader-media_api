from requests import get as requests_get
import logging
from time import sleep
from models.nebula.Streaming import NebulaVideoContentStreamingResponseModel
from models.urls import NEBULA_API_VIDEO_STREAM_INFORMATION


def get_streaming_information_by_episode(
    videoSlug: str,
    authorizationHeader: str,
    retryAfterUnsuccessfulSeconds: int = 5,
) -> NebulaVideoContentStreamingResponseModel:
    response = requests_get(
        url=NEBULA_API_VIDEO_STREAM_INFORMATION.format(VIDEO_SLUG=videoSlug),
        headers={
            "Authorization": authorizationHeader,
        },
    )
    logging.debug(
        "Received response of `%s...` with status code %s in %s seconds",
        response.content[:20],
        response.status_code,
        response.elapsed.total_seconds(),
    )
    if response.status_code == 200:
        return NebulaVideoContentStreamingResponseModel(**response.json())
    elif response.status_code == 403:
        logging.info(
            "The authorization token is invalid (got restricted), retrying in %s seconds... (status code: %s) (you should probably buy a new subscription or contact support)",
            retryAfterUnsuccessfulSeconds,
            response.status_code,
        )
        sleep(retryAfterUnsuccessfulSeconds)
        return get_streaming_information_by_episode(
            videoSlug=videoSlug,
            authorizationHeader=authorizationHeader,
            retryAfterUnsuccessfulSeconds=10,
        )
    elif response.status_code == 429:
        logging.warning(
            "Throttled by Nebula API while getting streaming information for `%s`, waiting for %s seconds...",
            videoSlug,
            retryAfterUnsuccessfulSeconds,
        )
        sleep(retryAfterUnsuccessfulSeconds)
        return get_streaming_information_by_episode(
            videoSlug=videoSlug,
            authorizationHeader=authorizationHeader,
            retryAfterUnsuccessfulSeconds=retryAfterUnsuccessfulSeconds + 1,
        )
    raise Exception(
        f"Failed to get video streaming info for `{videoSlug}` for an unknown reason: `{response.content[:32]}...` with status code {response.status_code}"
    )
