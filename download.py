from typing import Tuple
from config import VIDEOS_OUTPUT_DIRECTORY
from yt_dlp import YoutubeDL
from pathlib import Path
import json
import requests
from PIL import Image
from models import (
    NebulaVideoContentStreamingResponseModel,
)


def download_video(
    url: str, output_directory: Path, filename_output: str, quiet: bool = False
) -> None:
    ydl_opts = {
        "outtmpl": str(output_directory / filename_output),
        "format": "bestvideo+bestaudio/best",
        "quiet": quiet,
        "embedthumbnail": True,
        "embedsubtitle": True,
        "embeddescription": True,
        "embedchapters": True,
        "subtitleslangs": ["en", "de", "ru"],
        "convertthumbnails": "jpg",
        "max_filesize": 3900000000,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_thumbnail(
    url: str, output_file: Path, max_resolution: Tuple[int, int] = (320, 320)
) -> None:
    with open(output_file, "wb") as file:  # skipcq: PTC-W6004
        file.write(requests.get(url).content)
    img = Image.open(output_file)
    img.thumbnail(max_resolution, Image.Resampling.LANCZOS)
    img.save(output_file, format="JPEG", quality=70, optimize=True, progressive=True)


def main() -> None:
    for channel in VIDEOS_OUTPUT_DIRECTORY.iterdir():
        for episode in channel.iterdir():
            if episode.is_dir():
                with open(episode / "stream.json", "r") as file:
                    data = NebulaVideoContentStreamingResponseModel.parse_obj(
                        json.load(file)
                    )
                download_video(data.manifest, episode, episode.name + ".mp4")


if __name__ == "__main__":
    main()
