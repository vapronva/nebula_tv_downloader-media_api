from NebulaAPI import get_channel_video_content
from config import PARSE_NEBULA_CHANNLES_SLUGS, VIDEOS_OUTPUT_DIRECTORY
from models import NebulaChannelVideoContentDetails, NebulaChannelVideoContentEpisodes
import json


def create_channel_subdirectory_and_store_information(
    channel_slug: str,
    channel_data: NebulaChannelVideoContentDetails,
    episodes_data: NebulaChannelVideoContentEpisodes,
) -> None:
    channel_directory = VIDEOS_OUTPUT_DIRECTORY / channel_slug
    channel_directory.mkdir(parents=True, exist_ok=True)
    with open(channel_directory / "channel.json", "w") as file:
        json.dump(channel_data.dict(), file, indent=4)
    with open(channel_directory / "episodes.json", "w") as file:
        json.dump(episodes_data.dict(), file, indent=4)


def main() -> None:
    for channelSlug in PARSE_NEBULA_CHANNLES_SLUGS:
        channel_data = get_channel_video_content(channelSlug)
        create_channel_subdirectory_and_store_information(
            channelSlug, channel_data.details, channel_data.episodes
        )


if __name__ == "__main__":
    main()
