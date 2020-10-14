#!/usr/bin/python3

# Standard libraries.
import os
import json
import logging
import argparse

# Third party libraries.
# If these are missing, try running the command provided to install them.
import colorlog                   # python -m pip install colorlog
import tweepy as tw               # python -m pip install tweepy
from arrow import utcnow as now   # python -m pip install arrow

# Other Python files in this directory.
from authentication_data import *


# Setup the colored error message logger.
logger = logging.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

# Set up the argument parser.
parser = argparse.ArgumentParser(description="Get 10 random Tweets from a Twitter username.")
parser.add_argument('usernames', metavar="U", type=str, nargs='+',
                    help="A Twitter username, without the leading `@`.")
parser.add_argument('-v', '--verbose', action='count',
                    help="Set verbosity based on number of `v`s. `-v` = critical errors only; `-vvv` = default; `-vvvvv` = debug mode.")
parser.add_argument('-q', '--quiet', action='store_true',
                    help="All debug and error messages off. Overrides `-v`.")

# Some os and os.path nonsense.
pwd = os.path.dirname(os.path.abspath(__file__))
user_json_dir = os.path.join(pwd, "user_jsons/")

def users_overview(users):
    """Given a list of `User()` objects, prints some debug messages of
    interest about them."""

    for user in users:
        logger.debug("name: " + user.name)
        logger.debug("screen_name: " + user.screen_name)
        logger.debug("description: " + user.description)
        logger.debug("statuses_count: " + str(user.statuses_count))
        logger.debug("friends_count: " + str(user.friends_count))
        logger.debug("followers_count: " + str(user.followers_count))


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
    logger.info("Verbose mode enabled.")
    logger.debug("Arguments: {}".format(args))
    logger.debug("Present working directory: {}".format(pwd))
    logger.debug("User JSON files save location: {}".format(user_json_dir))

    if not os.path.exists(user_json_dir):
        logger.warning("User JSON file directory doesn't exist - attempting to create @ {}".format(user_json_dir))
        os.makedirs(user_json_dir)

    for data in auth_data:
        if len(data) == 0:
            logger.warning("A string in `authentication_data.py` is empty.")

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth_api = tw.API(auth)

    users = []
    for username in args.usernames:
        logger.info("Getting data from API for {}".format(username))
        users.append(auth_api.get_user(username))
        logger.info("{} acquired!".format(username))

    users_overview(users)

    # For the sake of making it easy to understand what the hell is going
    # on with User() objects, we dump them all into user_json_dir.

    timestamp = now().format('YYYY_MM_DD-HH_mm_ss')
    for user in users:
        path = os.path.join(user_json_dir, str(user.screen_name) + "__" + str(timestamp) + ".json")
        with open(path, 'w') as file:
            logger.debug("Writing JSON user data for {}, aka `@{}`, to {}.".format(user.name, user.screen_name, path))
            json.dump(user._json, file, indent=4, sort_keys=True)
