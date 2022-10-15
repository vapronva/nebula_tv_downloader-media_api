from typing import List
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
import json
from pathlib import Path

USER = Client(
    name="nebula-uploader-client",
    api_id=TELEGRAM_API_ID,
    api_hash=TELEGRAM_API_HASH,
    phone_number=TELEGRAM_USER_PHONENUMBER,
    no_updates=True,
)


def getEpisodeData(
    episode_slug: str, episode_list: List[NebulaChannelVideoContentEpisodeResult]
) -> NebulaChannelVideoContentEpisodeResult:
    for episode in episode_list:
        if episode.slug == episode_slug:
            return episode
    return None


def generateBeautifulDescription(descritpion: str, limitChars: int = 768) -> str:
    return (
        descritpion[:limitChars] + "..."
        if len(descritpion) > limitChars
        else descritpion
    )


def main() -> None:
    global USER
    USER.start()
    for channel in VIDEOS_OUTPUT_DIRECTORY.iterdir():
        epList: List[NebulaChannelVideoContentEpisodeResult] = [
            NebulaChannelVideoContentEpisodeResult.parse_obj(epifileinfo)
            for epifileinfo in json.load(open(channel / "episodes.json", "r"))
        ]
        for episodePath in channel.iterdir():
            if episodePath.is_dir():
                try:
                    with open(episodePath / "stream.json", "r") as file:
                        data = NebulaVideoContentStreamingResponseModel.parse_obj(
                            json.load(file)
                        )
                    download_video(
                        data.manifest, episodePath, episodePath.name + ".mp4"
                    )
                    epInfo = getEpisodeData(episodePath.name, epList)
                    USER.send_video(
                        chat_id=TELEGRAM_CHANNEL_ID,
                        video=Path(episodePath / (episodePath.name + ".mp4")).__str__(),
                        caption=f"""#{epInfo.channel_slug.replace('-', '_')} — <b>{epInfo.title}</b>
<i>{generateBeautifulDescription(epInfo.short_description, 384)}</i>

- Published on <code>{epInfo.published_at}</code>
- Duration: <code>{epInfo.duration}</code>
- Channel: <code>{epInfo.channel_title}</code>
- Share URL: {epInfo.share_url}
- Thumbnail URL: {epInfo.images.thumbnail.src}
- Attributes: <code>{epInfo.attributes}</code>
- Categories: <code>{epInfo.category_slugs}</code>""",
                        disable_notification=True,
                        file_name=f"{epInfo.slug}.mp4",
                    )
                    Path(episodePath / (episodePath.name + ".mp4")).unlink()
                except Exception as e:
                    print(e)
                    USER.stop()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        USER.stop()
