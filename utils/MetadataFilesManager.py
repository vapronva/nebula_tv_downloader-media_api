import json
from pathlib import Path
from models.nebula.Channel import NebulaChannelVideoContentDetails
from models.nebula.Fetched import NebulaChannelVideoContentEpisodes


def create_channel_subdirectory_and_store_metadata_information(
    channelSlug: str,
    channelData: NebulaChannelVideoContentDetails,
    episodesData: NebulaChannelVideoContentEpisodes,
    outputDirectory: Path,
) -> Path:
    channelDirectory = outputDirectory / channelSlug
    channelDirectory.mkdir(parents=True, exist_ok=True)
    with open(channelDirectory / "channel.json", "w") as file:
        json.dump(channelData.dict(), file, indent=4)
    with open(channelDirectory / "episodes.json", "w") as file:
        json.dump(episodesData.dict()["results"], file, indent=4)
    return channelDirectory
