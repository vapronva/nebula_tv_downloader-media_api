from yt_dlp import YoutubeDL
from pathlib import Path
import requests
from PIL import Image
from models.nebula.Streaming import NebulaVideoContentStreamSubtitles
from urllib.parse import urlparse


def download_video(
    url: str,
    outputFile: Path,
    quiet: bool = False,
    downloadFormat: str = "bestvideo+bestaudio/best",
    maxFileSize: int | None = None,
    subtitleLanguages: list[str] = ["en", "de", "ru"],  # skipcq: PYL-W0102
) -> None:
    ydl_opts = {
        "outtmpl": outputFile.__str__() + ".%(ext)s",
        "format": downloadFormat,
        "quiet": quiet,
        "embedthumbnail": True,
        "embedsubtitle": True,
        "embeddescription": True,
        "embedchapters": True,
        "subtitleslangs": subtitleLanguages,
        "convertthumbnails": "jpg",
        "max_filesize": maxFileSize,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return


def download_thumbnail(
    url: str,
    outputFile: Path,
    maxResolution: tuple[int, int] | None = None,
    compressImage: bool = False,
) -> None:
    with open(outputFile, "wb") as file:  # skipcq: PTC-W6004
        file.write(requests.get(url).content)
    if compressImage:
        img = Image.open(outputFile)
        if maxResolution is not None:
            img.thumbnail(maxResolution, Image.Resampling.LANCZOS)
        img.save(outputFile, format="JPEG", quality=85, optimize=True, progressive=True)
    return


def download_subtitles(
    subtitiles: list[NebulaVideoContentStreamSubtitles],
    outputDirectory: Path,
) -> None:
    for subtitle in subtitiles:
        outputName: str = (
            subtitle.language_code
            + "-"
            + urlparse(subtitle.url)
            .path.split("/")[-1]
            .replace("-", "_")
            .replace(".", "_")
        )
        outputFilename: Path = outputDirectory / outputName
        with open(outputFilename, "wb") as file:
            file.write(requests.get(subtitle.url).content)
    return
