#!/usr/bin/python3


import logging
import colorlog                   # python -m pip install colorlog
import tweepy as tw               # python -m pip install tweepy

from authentication_data import *

# Setup

logger = logging.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)



if __name__ == "__main__":
    logger.info("Hello, TenTweetsFrom.")
    logger.info("-" * 70)

    for data in auth_data:
        if len(data) == 0:
            logger.warning("A string in `authentication_data.py` is empty.")

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = tw.API(auth)
