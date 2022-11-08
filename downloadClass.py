from pathlib import Path
from typing import List
from NebulaAPI import get_authorization_token
import requests
from config import (
    HTTP_API_CLASS_SLUG_INFORMATION,
    TOKEN_NEBULA_USERAPI_AUTHORIZATION,
    VIDEOS_OUTPUT_DIRECTORY,
    NEBULA_API_CLASS_STREAM_INFORMATION,
)
import json
from download import download_video

ALL_CLASS_SLUGS: List[str] = []

for CLASS_SLUG in ALL_CLASS_SLUGS:
    # CLASS_SLUG: str = "high-spec-content-on-a-low-spec-budget"
    response = requests.get(
        url=HTTP_API_CLASS_SLUG_INFORMATION.format(
            CLASS_SLUG=CLASS_SLUG, CLASS_NUMBER=1
        ),
        headers={
            "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
        },
    )
    if response.status_code != 200:
        print(response.status_code, response.content)
        raise Exception("Unable to get class information")
    outputDirectory: Path = VIDEOS_OUTPUT_DIRECTORY / CLASS_SLUG
    outputDirectory.mkdir(parents=True, exist_ok=True)
    with open(outputDirectory / "class.json", "w") as f:
        json.dump(response.json()["class"], f, indent=4)
    for classInformation in response.json()["class"]["lessons"]:
        className: str = (
            f"nebula-{CLASS_SLUG.replace('-', '_')}-{classInformation['order']}"
        )
        print(className)
        response = requests.get(
            url=NEBULA_API_CLASS_STREAM_INFORMATION.format(
                CLASS_SLUG=CLASS_SLUG, CLASS_NUMBER=classInformation["order"]
            ),
            headers={
                "Authorization": f"Bearer {get_authorization_token(TOKEN_NEBULA_USERAPI_AUTHORIZATION)}",
            },
        )
        if response.status_code != 200:
            print(response.status_code, response.content)
            raise Exception("Unable to get class information")
        dataStream = response.json()
        streamingURL: str = dataStream["manifest"]
        with open(outputDirectory / f"{className}-stream.json", "w") as f:
            json.dump(dataStream, f, indent=4)
        download_video(streamingURL, outputDirectory, f"{className}.mp4")
