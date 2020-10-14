#!/usr/bin/python3


import logging
import colorlog                   # python -m pip install colorlog
import tweepy as tw               # python -m pip install tweepy

# Setup

logger = logging.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)


if __name__ == "__main__":
    logger.info("Hello, TenTweetsFrom.")
    logger.info("-" * 80)
