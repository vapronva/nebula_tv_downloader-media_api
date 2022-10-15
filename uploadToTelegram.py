from typing import List, Optional, Tuple
from pyrogram import Client
from config import (
    TELEGRAM_API_ID,
    TELEGRAM_API_HASH,
    TELEGRAM_USER_PHONENUMBER,
    TELEGRAM_CHANNEL_ID,
    VIDEOS_OUTPUT_DIRECTORY,
)
from models import (
    NebulaVideoContentStreamingResponseModel,
    NebulaChannelVideoContentEpisodeResult,
)
from download import download_video, download_thumbnail
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import logging


USER = Client(
    name="nebula-uploader-client",
    api_id=TELEGRAM_API_ID,
    api_hash=TELEGRAM_API_HASH,
    phone_number=TELEGRAM_USER_PHONENUMBER,
    no_updates=True,
)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def getEpisodeData(
    episode_slug: str, episode_list: List[NebulaChannelVideoContentEpisodeResult]
) -> NebulaChannelVideoContentEpisodeResult:
    for episode in episode_list:
        if episode.slug == episode_slug:
            return episode
    return None


def process_video(
    epInfo: NebulaChannelVideoContentEpisodeResult,
    episodePath: Path,
    epList: Optional[List[NebulaChannelVideoContentEpisodeResult]],
    SEND_VIDEO: bool = True,
) -> None:
    try:
        with open(episodePath / "stream.json", "r") as file:
            data = NebulaVideoContentStreamingResponseModel.parse_obj(json.load(file))
        logging.info("Downloading video `%s`...", epInfo.slug)
        download_video(data.manifest, episodePath, episodePath.name + ".mp4", True)
        download_thumbnail(epInfo.images.thumbnail.src, Path(episodePath / "thumb.jpg"))
        logging.info("Sendong video `%s` to Telegram...", epInfo.slug)
        if SEND_VIDEO:
            USER.send_video(
                chat_id=TELEGRAM_CHANNEL_ID,
                video=Path(episodePath / (episodePath.name + ".mp4")).__str__(),
                caption=f"""#{epInfo.channel_slug.replace('-', '_')} — <b>{epInfo.title}</b>
<i>{epInfo.short_description[:384]}</i>

- Published on <code>{epInfo.published_at}</code>
- Duration: <code>{epInfo.duration}</code>
- Channel: <code>{epInfo.channel_title}</code>
- Share URL: {epInfo.share_url}
- Thumbnail URL: {epInfo.images.thumbnail.src}
- Attributes: <code>{epInfo.attributes}</code>
- Categories: <code>{epInfo.category_slugs}</code>""",
                disable_notification=True,
                file_name=f"{epInfo.slug}.mp4",
                thumb=open(Path(episodePath / "thumb.jpg").__str__(), "rb"),
            )
            logging.info("Video `%s` sent to Telegram!", epInfo.slug)
            Path(episodePath / (episodePath.name + ".mp4")).unlink()
            logging.info(
                "Episode `%s` processed! (out of %s)",
                epInfo.slug,
                str(len(epList)),
            )
    except Exception as e:  # skipcq: PYL-W0703
        print(e)


def process_channel_batch(
    episodesList: List[
        Tuple[
            NebulaChannelVideoContentEpisodeResult,
            Path,
            List[NebulaChannelVideoContentEpisodeResult],
        ]
    ],
    SEND_VIDEO: bool = False,
) -> None:
    for episode in episodesList:
        process_video(episode[0], episode[1], episode[2], SEND_VIDEO)


def main() -> None:
    global USER
    USER.start()
    totalEpisodes: int = 0
    OUTPUT_CHANNELS: List[
        List[
            Tuple[
                NebulaChannelVideoContentEpisodeResult,
                Path,
                List[NebulaChannelVideoContentEpisodeResult],
            ]
        ]
    ] = []
    for channel in sorted(VIDEOS_OUTPUT_DIRECTORY.iterdir()):
        epList: List[NebulaChannelVideoContentEpisodeResult] = [
            NebulaChannelVideoContentEpisodeResult.parse_obj(epifileinfo)
            for epifileinfo in json.load(open(channel / "episodes.json", "r"))
        ]
        OUTPUT_EPISODES: List[
            Tuple[
                NebulaChannelVideoContentEpisodeResult,
                Path,
                List[NebulaChannelVideoContentEpisodeResult],
            ]
        ] = []
        for episodePath in channel.iterdir():
            if episodePath.is_dir():
                epInfo = getEpisodeData(episodePath.name, epList)
                OUTPUT_EPISODES.append((epInfo, episodePath, epList))
        OUTPUT_CHANNELS.append(OUTPUT_EPISODES)
        totalEpisodes += 1
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(process_channel_batch, OUTPUT_CHANNELS)
    for channel in OUTPUT_CHANNELS:
        process_channel_batch(channel, True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        USER.stop()
