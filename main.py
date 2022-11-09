import logging
from config.Config import Config
from NebulaAPI.Authorization import NebulaUserAuthorzation
from NebulaAPI.VideoFeedFetcher import get_all_channels_slugs_from_video_feed
from utils.Filtering import filter_out_episodes
from models.nebula.Fetched import NebulaChannelVideoContentEpisodeResult

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

CONFIG = Config()

NEBULA_AUTH = NebulaUserAuthorzation(
    userToken=CONFIG.NebulaAPI.USER_API_TOKEN,
    authorizationHeader=CONFIG.NebulaAPI.AUTHORIZATION_HEADER,
)


def main() -> None:
    result = get_all_channels_slugs_from_video_feed(
        authorizationHeader=NEBULA_AUTH.get_authorization_header(full=True),
        categoryFeedSelector=CONFIG.NebulaFilters.CATEGORY_SEARCH,
        cursorTimesLimitFetchMaximum=1,
        okShouldReturnAllEpisodesListActually=True,
    )
    if len(result) > 0:
        if isinstance(result[0], NebulaChannelVideoContentEpisodeResult):
            try:
                episodes: list[
                    NebulaChannelVideoContentEpisodeResult
                ] = result  # type: ignore
            except Exception:
                raise Exception(
                    f"Failed to cast episodes to `list[NebulaChannelVideoContentEpisodeResult]`"
                )
            episodes = list(
                filter_out_episodes(
                    filterSettings=CONFIG.NebulaFilters,
                    episodes=episodes,
                )
            )
            logging.debug("Filtered %s episodes", len(episodes))


if __name__ == "__main__":
    main()
