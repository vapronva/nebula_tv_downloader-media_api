from yt_dlp import YoutubeDL
from pathlib import Path
import json
import requests
from PIL import Image


def download_video(
    url: str,
    outputFile: Path,
    quiet: bool = False,
    downloadFormat: str = "bestvideo+bestaudio/best",
    maxFileSize: int | None = None,
    subtitleLanguages: list[str] = ["en", "de", "ru"],
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
    }
    ydl_opts["max_filesize"] = maxFileSize if maxFileSize is not None else None
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
        img.thumbnail(
            maxResolution, Image.Resampling.LANCZOS
        ) if maxResolution is not None else None
        img.save(outputFile, format="JPEG", quality=85, optimize=True, progressive=True)
    return
