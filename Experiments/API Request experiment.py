# 11/11/2020 - API Request experiment
# The objective of this project is for a user to find out about a game by entering its name.
# The process goes as follows:
# The user will enter the name of a steam game
# A list of relevant ids (and the game names) will be returned and the user will choose the one that's relevant
## (The queried games will show up in this format: id##### - GameName (Steam Release Year) )
# [NOTE] For subsequent searches, the program will search through the already-stored "database"
# [NOTE] The user can also update the stored database by selecting that option in the menu.
# [NOTE] The program will display the date in which the database was last updated.
# [Tasks]
## Add a menu interface
## Include the update method (which will either grab or read from a large json file)

import time
import json
import os
import sys
import requests
# from tkinter import filedialog

appDetailsLink = "https://store.steampowered.com/api/appdetails?appids="
appID = 10

def InputCheck(phrase, optionlist, options):
    string = (phrase + "\n-----[OPTIONS]-----\n")
    for i in range(len(optionlist)):
        string += (str(optionlist[i]) + "\n")
    while True:
        text = str(input(string)).lower()
        if text in options:
            return text
            string = ""
        else:
            print("{Error. Select a valid option.}")

try:
    appID = int(input("Enter the steam id of a game you want the details of:\n"))
except ValueError:
    print("Enter an integer for the steam id. Don't enter letters, symbols, or decimals.")
else:
    print("--- Starting search ---")


try:
    r = requests.get(str(appDetailsLink) + str(appID))
    attemptTime = time.time()
except ConnectionError:
    print("[CONNECTION ERROR] Something's wrong. \n" + str(r.status_code))
except TimeoutError:
    print("[REQUEST TIMED OUT] Something's wrong. \n" + str(r.status_code))
else:
    print("***[REQUEST SUCCESSFUL]***")
    print(r.headers)
    print("Process duration: " + str(time.time() - attemptTime))
AppsJson = r.json()


with open(os.path.join(sys.path[0], 'SteamApps.json'), 'w', encoding='utf-8') as SteamApps:
    json.dump(AppsJson, SteamApps, ensure_ascii=False, indent=4)
    print("Data appended to file.")

with open(os.path.join(sys.path[0], 'SteamApps.json'), 'r', encoding='utf-8') as SteamApps:
    data = json.load(SteamApps)
    Type = data[str(appID)]['data'].get('type')
    name = data[str(appID)]['data'].get('name')
    shortDesc = data[str(appID)]['data'].get('short_description')
    ageRating = data[str(appID)]['data'].get('required_age')
    controllerSupport = data[str(appID)]['data'].get('controller_support')
    countDLC = data[str(appID)]['data'].get('dlc')
    developers = data[str(appID)]['data'].get('developers')
    publishers = data[str(appID)]['data'].get('publishers')
    if str(data[str(appID)]['data'].get('is_free')).lower() == "true":
        price = "Free"
    else:
        price = data[str(appID)]['data']['price_overview'].get('final_formatted')
    if not data[str(appID)]['data'].get('achievements'):
        achievements = "N/A"
    else:
        achievements = str(data[str(appID)]['data']['achievements'].get('total')) + " achievements"
    players = "N/A - Need to work on this"
    genres = []
    for genre in data[str(appID)]['data'].get('genres'):
        genres.append(genre.get('description'))
    print("==============================")
    print(str(appID) + " - " + str(name) + " - (" + str(appID) + ")")
    print("[Type:] " + str(Type))
    print("[Age Req.:] " + str(ageRating))  # INCOMPLETE
    if data[str(appID)]['data']['price_overview'].get('discount_percent') > 0:
        print("[Price:] " + str(price) + " (" +
              str(data[str(appID)]['data']['price_overview'].get('discount_percent')) + "% off, " +
              str(data[str(appID)]['data']['price_overview'].get('initial_formatted')) + " initially)")
    else:
        print("[Price:] " + str(price))
    print("[Desc:] " + str(shortDesc))
    print("[Developer(s):] " + ','.join(developers))
    print("[Publisher(s):] " + ','.join(publishers))
    print("[Controller Support:] " + str(controllerSupport))
    print("[Achievements:] " + str(achievements))
    print("[Players:] " + str(players))  # INCOMPLETE
    print("[Genres:] " + ','.join(genres))
    print("[DLC:] " + str(countDLC))  # INCOMPLETE
    print("==============================")
#    userInput = InputCheck("", ["[1] - Search another game", "[2] - Exit"], ["1", "2"])
