from typing import Generator
from models.configuration import ConfigurationNebulaFiltersModel
from models.nebula.Episode import NebulaChannelVideoContentEpisodeResult
from models.nebula.VideoAttributes import VideoNebulaAttributes


def filter_out_episodes(
    filterSettings: ConfigurationNebulaFiltersModel,
    episodes: list[NebulaChannelVideoContentEpisodeResult],
) -> Generator[NebulaChannelVideoContentEpisodeResult, None, None]:
    for episode in episodes:
        if (
            filterSettings.INCLUDE_NEBULA_FIRST
            and VideoNebulaAttributes.IS_NEBULA_FIRST not in episode.attributes
        ):
            continue
        if (
            filterSettings.INCLUDE_NEBULA_PLUS
            and VideoNebulaAttributes.IS_NEBULA_PLUS not in episode.attributes
        ):
            continue
        if not filterSettings.INCLUDE_REGULAR_VIDEOS:
            continue
        yield episode
