#!/usr/bin/python3


import logging
import colorlog                   # python -m pip install colorlog
import tweepy as tw               # python -m pip install tweepy
import argparse

from authentication_data import *

# Setup the colored error message logger.
logger = logging.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

# Set up the argument parser.
parser = argparse.ArgumentParser(description="Get 10 random Tweets from a Twitter username.")
parser.add_argument('username', metavar='U', type=str, nargs=1,
                    help="A single Twitter username, without the leading `@`.")
parser.add_argument('-v', '--verbose', action='count',
                    help="Set verbosity based on number of `v`s. `-v` = critical errors only; `-vvv` = default; `-vvvvv` = debug mode.")
parser.add_argument('-q', '--quiet', action='store_true',
                    help="All debug and error messages off. Overrides `-v`.")


def set_verbosity(args):
    """Given a `Namespace()` with a `verbose` and a `quiet` variable,
    sets the global logger debug level.

    If args.quiet=True, logging is turned off entirely. This overrides
    everything else. You could actually turn it back on later by setting

            logger.disabled = False

    if you wanted to oscillate between no logs at all and, say, DEBUG level
    like a crazy person.

    verbose=None keeps it at WARNING. Otherwise we use an explicit count."""
    if args.quiet:
        logger.disabled = True

    if args.verbose is None:
        return None
    elif args.verbose == 1:
        return logger.setLevel(colorlog.colorlog.logging.CRITICAL)
    elif args.verbose == 2:
        return logger.setLevel(colorlog.colorlog.logging.ERROR)
    elif args.verbose == 3:
        return logger.setLevel(colorlog.colorlog.logging.WARNING)
    elif args.verbose == 4:
        return logger.setLevel(colorlog.colorlog.logging.INFO)
    elif args.verbose >= 5:
        return logger.setLevel(colorlog.colorlog.logging.DEBUG)
    else:
        return None


if __name__ == "__main__":
    args = parser.parse_args()
    set_verbosity(args)

    logger.debug("Arguments: {}".format(args))

    for data in auth_data:
        if len(data) == 0:
            logger.warning("A string in `authentication_data.py` is empty.")

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = tw.API(auth)
