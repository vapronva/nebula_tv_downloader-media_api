from typing import Generator
from models.configuration import ConfigurationNebulaFiltersModel
from models.nebula.Episode import NebulaChannelVideoContentEpisodeResult
from models.nebula.VideoAttributes import VideoNebulaAttributes
import logging


def filter_out_episodes(
    filterSettings: ConfigurationNebulaFiltersModel,
    episodes: list[NebulaChannelVideoContentEpisodeResult],
) -> Generator[NebulaChannelVideoContentEpisodeResult, None, None]:
    applicableFilters: list[VideoNebulaAttributes] = []
    if filterSettings.INCLUDE_NEBULA_ORIGINALS:
        applicableFilters.append(VideoNebulaAttributes.IS_NEBULA_ORIGINAL)
    if filterSettings.INCLUDE_NEBULA_PLUS:
        applicableFilters.append(VideoNebulaAttributes.IS_NEBULA_PLUS)
    if filterSettings.INCLUDE_NEBULA_FIRST:
        applicableFilters.append(VideoNebulaAttributes.IS_NEBULA_FIRST)
    logging.debug("Applicable filters: %s", applicableFilters)
    logging.debug("Include regular videos: %s", filterSettings.INCLUDE_REGULAR_VIDEOS)
    for episode in episodes:
        if applicableFilters:
            if any(filter in episode.attributes for filter in applicableFilters):
                yield episode
                continue
        if filterSettings.INCLUDE_REGULAR_VIDEOS and (
            not episode.attributes
            or [VideoNebulaAttributes.FREE_SAMPLE_ELIGIBLE] == episode.attributes
        ):
            yield episode
            continue
        continue
