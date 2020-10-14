#!/usr/bin/python3

from time import sleep
import os


# This is just a container for the data you'll need to authenticate with
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


def beat(t=1):
    sleep(t)
    print("")
    sleep(t)
    return None

if __name__ == "__main__":
    print("Here the data you are currently authenticating with.")
    print("If these are empty, you will need to create a Twitter")
    print("application and get these.")

    beat()

    print("Consumer Key :: {}".format(consumer_key))
    print("Consumer Secret :: {}".format(consumer_secret))
    print("Access Token :: {}".format(access_token))
    print("Access Token Secret :: {}".format(access_token_secret))

    beat()


    print("**Letting this data be seen publicly is a security risk.**")

    beat()

    print("If you're worried about forking this and accidentally pushing")
    print("your private data, I strongly recommend you navigate to this")
    print("directory and run the commend,")

    beat()

    print("    git update-index --assume-unchanged authentication_data.py")

    beat()

    print("This will make it so git stops tracking this file on your PC.")


    beat()

    print("    git update-index --no-assume-unchanged authentication_data.py")

    beat()

    print("will reverse this process.")

    beat()
    
    print("-" * 80)
