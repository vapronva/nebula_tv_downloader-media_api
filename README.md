# [Nebula.tv](https://nebula.tv) Video Archiver

> — *this video is brought to you by nebula!* \
> — *who the hell is nebula?* \
> — *nebula deez…*

## Warning / Prerequisites

### Violation of Nebula's Terms of Service

⚠️ Poking at Nebula API in non-official ways will most likely result in a **Nebula subscription taken out on your account**. Use at your own risk.

### This is a Proof of Concept

Everything was written and tested in one day. It's not perfect, it's not pretty, it's not even complete.

### Subscription

You need a Nebula subscription to use this tool.

You can buy one on official website ([nebula.tv](https://nebula.tv)), via influencers' referral links, via CuriosityStream ([curiositystream.com/nebula](https://curiositystream.com/nebula)).

## What is This?

Simple project that will parse and download *all* videos from Nebula channels (or from a selection of channels).

### Why?

If you can find inifinite money glitch, you can just download every video on Nebula. But if you can't, you can still download all videos from a channel you like. \
Also, having a local copy of online-videos on a streaming service is a good idea, in case the service goes down.

## How to Use

1. In the cloned repository, define certain values in the `config.py` file (only `TOKEN_NEBULA_USERAPI_AUTHORIZATION` is required).
2. Install necessary dependencies for Python from `requirements.txt`.
3. Run `main.py` to download all channel information and episodes streaming links.
4. Run `download.py` to download all parsed episodes. Or run `uploadToTelegram.py` to upload all parsed episodes to Telegram (no videos are stored on the local machine).

### Getting Nebula API Token

1. Open Nebula website in your browser.
2. Reload any page with inspector open.
3. Find a request made to `/api/v1/authorization/`.
4. Copy the value of `Authorization` header without the `Token` keyword.
