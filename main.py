from pathlib import Path
from NebulaAPI import (
    get_channel_video_content,
    get_straming_info,
    get_all_channels_from_video_feed,
)
from config import PARSE_NEBULA_CHANNLES_SLUGS, VIDEOS_OUTPUT_DIRECTORY
from models import (
    NebulaChannelVideoContentDetails,
    NebulaChannelVideoContentEpisodes,
    NebulaVideoContentStreamingResponseModel,
)
import logging
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
        json.dump(episodes_data.dict()["results"], file, indent=4)


def save_episode_streaming_information(
    channel_slug: str,
    episode_slug: str,
    stream_data: NebulaVideoContentStreamingResponseModel,
) -> None:
    channel_directory = VIDEOS_OUTPUT_DIRECTORY / channel_slug
    episode_directory = channel_directory / episode_slug
    episode_directory.mkdir(parents=True, exist_ok=True)
    with open(episode_directory / "stream.json", "w") as file:
        json.dump(stream_data.dict(), file, indent=4)


def main() -> None:
    global PARSE_NEBULA_CHANNLES_SLUGS  # skipcq: PYL-W0603
    if len(PARSE_NEBULA_CHANNLES_SLUGS) == 0:
        PARSE_NEBULA_CHANNLES_SLUGS = get_all_channels_from_video_feed()
    for channelSlug in PARSE_NEBULA_CHANNLES_SLUGS:
        channel_data = get_channel_video_content(channelSlug)
        create_channel_subdirectory_and_store_information(
            channelSlug, channel_data.details, channel_data.episodes
        )
        logging.info("Saved channel information for `%s` to disk", channelSlug)
        for episode in channel_data.episodes.results:
            if not Path(VIDEOS_OUTPUT_DIRECTORY / channelSlug / episode.slug).exists():
                save_episode_streaming_information(
                    channelSlug, episode.slug, get_straming_info(episode.slug)
                )
                logging.info("Saved episode information for `%s` to disk", episode.slug)
                continue
            logging.info(
                "Skipping episode `%s` for channel `%s` as it already exists",
                episode.slug,
                channelSlug,
            )


if __name__ == "__main__":
    main()
