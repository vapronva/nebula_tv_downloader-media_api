# [Nebula.tv](https://nebula.tv) Video Archiver

> — *this video is brought to you by nebula!* \
> — *who the hell is nebula?* \
> — *nebula deez…*

## Warning / Prerequisites

### Violation of Nebula's Terms of Service *(?)*

⚠️ Poking at Nebula API in non-official ways will most likely result in a **Nebula subscription taken out on your account**. Use at your own risk.

### Subscription

You need a Nebula subscription to use this tool.

You can buy one on official website ([nebula.tv](https://nebula.tv)), via influencers' referral links, via CuriosityStream ([curiositystream.com/nebula](https://curiositystream.com/nebula)).

### Limitations

There are currently no known limitations to the number of videos you can download from the Nebula.

But there are some limitations in this tool:

- The tool internal logic is based on the assumption that you want to download *all* the videos from a given channel;
- No user agent spoofing (since Nebula API doesn't seem to care about it, but it will be added in the future);
- No multi-threading by design (just to be on the safe side);
- No Classes downloader (but will be added in the future).

## What is This?

Simple project that will parse and download *all* videos from Nebula channels (or from a selection of channels).

### Why?

If you can find inifinite money glitch, you can just download every video on Nebula. But if you can't, you can still download all videos from a channel you like. \
Also, having a local copy of online-videos on a streaming service is a good idea, in case the service goes down.

## How to Use

1. In the cloned repository, in the `config/` directory copy example config (`config.example.ini`) to the `config.ini`, define certain values in the `config.ini` file (only `USER_API_TOKEN` is required).
2. Install necessary dependencies for Python from the `requirements.txt`.
3. Run `main.py` (from the root of the repository).

### Getting Nebula API Token

1. Open Nebula website in your browser.
2. Reload any page with inspector open.
3. Find a request made to `/api/v1/authorization/`.
4. Copy the value of `Authorization` header without the `Token` keyword.

### Configuration File

The configuration file is located in `config/config.ini`. \
The file is self-explanatory, but here are some notes:

```ini
[NebulaAPI]
USER_API_TOKEN = <nebula user token> ; Nebula API token (see above). Required.
[NebulaFilters]
CATEGORY_SEARCH = false ; If set to `false`, the filter is disabled, otherwise it is enabled and the contents are applied to search. Example: `CATEGORY_SEARCH = originals` will result in adding `?category=originals` to the search query. Recommended values: `originals`, `false`.
INCLUDE_NEBULA_FIRST = false ; Whether to include "Nebula First" videos in the filtration. Possible values: `true`, `false`.
INCLUDE_NEBULA_PLUS = true ; Whether to include "Nebula Plus" videos in the filtration. Possible values: `true`, `false`.
INCLUDE_NEBULA_ORIGINALS = true ; Whether to include "Nebula Originals" videos in the filtration. Possible values: `true`, `false`.
INCLUDE_REGULAR_VIDEOS = false ; Whether to include all other videos in the filtration. Possible values: `true`, `false`.
CHANNELS_TO_PARSE = ; If the variable is set to empty string, the feed searcher is disabled, otherwise it is parsed and is only these channels are searched. Example: `CHANNELS_TO_PARSE = jetlag,reallifelore`
[Downloader]
DOWNLOAD_PATH = ./output ; Path to the directory where the videos will be downloaded. The directory will be created if it doesn't exist.
```
