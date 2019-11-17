# taxi (alpha)
## The cheapest taxi proposal finder
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/565cdc1bc69544878c7f18a92b7566a7)](https://www.codacy.com/manual/antonkurenkov/taxi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=antonkurenkov/taxi&amp;utm_campaign=Badge_Grade)

This is a [Telegram bot][tele] for searching the cheapest proposal for the given route.

## Description

It crawls five popular taxi service providers and gives you proposals to choose from.

## Setup

The app is written in Python 3.7.4, so you need a proper version be installed.
It depends on following libs, so you also need:

-   `selenium`
-   `telebot`
-   `datetime`
-   `multiprocessing`
-   `re`

Input your telegram bot token into the `bot.py` in the main folder.

## Run

Just run the `bot.py` file for bot to start.

## Usage

You give the `start` and `finish` points for the bot, it returns you the best proposal for the given route.

The bot runs in the background so you should leave the shell window opened.

It uses `multiprocessing` lib for parsing all the taxi services at the same time, so you could get responses in different order.

[tele]: https://github.com/mullwar/telebot