# 4/5/2021 - Lyrics Finder
# The goal of this program is to find quickly find the lyrics to a music track.
# This particular program uses lyrics.ovh

import requests
import sys

while True:
    artist = input("Enter an artist name\n")
    title = input("Enter the track you want lyrics for\n")

    response = requests.get("https://api.lyrics.ovh/v1/" + artist + "/" + title)
    json_response = response.json()

    if response.status_code is 200:
        print(artist + " - " + title)
        print(json_response["lyrics"])
        print("----------------------------------------------------------")
    elif response.status_code is 404:
        print("Sorry, but there aren't any lyrics for this track from lyrics.ovh")
    else:
        print("We failed to acquire lyrics for '" + artist + " - " + title + "'\n(Error: " + str(response.status_code)
              + ")")

    try:
        user_input = input("Would you like to get lyrics for another track? (Please type 1 or 2)\n1 - Yes\n2 - No\n")
    except:
        if user_input != "1" or "2":
            print("Please type 1 or 2")
    if user_input is "2":
        sys.exit()
