from models import (
    NebulaChannelVideoContentResponseModel,
    NebulaUserAPIAuthorizationTokenResponseModel,
)
from config import *
import requests
import logging

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
        return NebulaChannelVideoContentResponseModel(**response.json())
    raise Exception(
        f"Failed to get channel video content: {response.content} with status code {response.status_code}"
    )


def main():
    CHANNEL_SLUG = "techaltar"
    print(get_channel_video_content(CHANNEL_SLUG))


if __name__ == "__main__":
    main()
