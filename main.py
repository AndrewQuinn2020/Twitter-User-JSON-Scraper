#!/usr/bin/python3

import logging     # installed by default
import colorlog    # run python -m pip install colorlog

# Setup

logger = logging.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)


if __name__ == "__main__":
    logger.debug("Hello, TenTweetsFrom.")
