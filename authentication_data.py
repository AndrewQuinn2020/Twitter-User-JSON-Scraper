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

    print("That's why this file is listed in `.gitignore` -- so long as")
    print("you don't remove `authentication_data.py` from `.gitignore`,")
    print("you won't accidentally `git push` it yourself.")

    beat()

    print("Let's check to make sure it's still there...")

    beat()

    gitignore_path = os.path.join(os.path.dirname(__file__), ".gitignore")

    print("Scanning for `authentication_data.py` in\n\n\t{}\n\n...\n\n".format(gitignore_path))

    beat()

    with open(gitignore_path, 'r') as file:
        it_was_there = False
        for line in file:
            if "authentication_data.py" in line:
                print("We got it!")
                it_was_there = True
                break
        if not it_was_there:
            print("Oh, we couldn't find it. Double check if you're worried!")

    beat()

    print("-" * 80)
