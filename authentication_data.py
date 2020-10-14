#!/usr/bin/python3

from time import sleep
import os


# This is just a container for the data you'll need to authenticate with
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth_data = [consumer_key, consumer_secret, access_token, access_token_secret]


if __name__ == "__main__":
    print("-" * 80)

    print("Here the data you are currently authenticating with.")
    print("If these are empty, you will need to create a Twitter")
    print("application and get these.")
    print("If you're having trouble finding them, try")
    print("")
    print("    https://developer.twitter.com/en/apps/")
    print("")
    print("and see if anything comes up for you. You might need to apply")
    print("for a Twitter Developer account and make an app there if you're")
    print("new!")
    print("")
    print("(Note this was written October 14, 2020)")

    print("")

    print("Consumer Key        :: {}".format(consumer_key))
    print("Consumer Secret     :: {}".format(consumer_secret))
    print("Access Token        :: {}".format(access_token))
    print("Access Token Secret :: {}".format(access_token_secret))

    print("")


    print("**Letting this data be seen publicly is a security risk.**")

    print("")

    print("If you're worried about forking this and accidentally pushing")
    print("your private data, I strongly recommend you navigate to this")
    print("directory and run the commend,")

    print("")

    print("    git update-index --assume-unchanged authentication_data.py")

    print("")

    print("This will make it so git stops tracking this file on your PC.")

    print("")

    print("    git update-index --no-assume-unchanged authentication_data.py")

    print("")

    print("will reverse this process.")

    print("-" * 80)
