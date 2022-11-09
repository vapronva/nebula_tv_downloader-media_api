from typing import Generator
import logging
from models.configuration import ConfigurationNebulaFiltersModel
from models.nebula.Episode import NebulaChannelVideoContentEpisodeResult
from models.nebula.VideoAttributes import VideoNebulaAttributes


def filter_out_episodes(
    filterSettings: ConfigurationNebulaFiltersModel,
    episodes: list[NebulaChannelVideoContentEpisodeResult],
) -> Generator[NebulaChannelVideoContentEpisodeResult, None, None]:
    applicableFilters: list[VideoNebulaAttributes] = []
    applicableFilters.append(
        VideoNebulaAttributes.IS_NEBULA_ORIGINAL
    ) if filterSettings.INCLUDE_NEBULA_ORIGINALS else None
    applicableFilters.append(
        VideoNebulaAttributes.IS_NEBULA_PLUS
    ) if filterSettings.INCLUDE_NEBULA_PLUS else None
    applicableFilters.append(
        VideoNebulaAttributes.IS_NEBULA_FIRST
    ) if filterSettings.INCLUDE_NEBULA_FIRST else None
    for episode in episodes:
        if applicableFilters:
            if any([filter in episode.attributes for filter in applicableFilters]):
                yield episode
        else:
            if filterSettings.INCLUDE_REGULAR_VIDEOS:
                yield episode
        continue
