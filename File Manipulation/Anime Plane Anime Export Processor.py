# 8/4/2020 Anime Plane Anime Export Processor
# The purpose of this program is to process all of the anime data from a JSON file into a neat and organized text file.
# Tasks
## Alphabetically organize objects

import json
import datetime
import os
from tkinter import filedialog

name = filedialog.askopenfilename()
nameProcessed = os.path.splitext(os.path.basename(name))[0]
count = 0
time = datetime.datetime.now()

with open(name) as json_file:
    data = json.load(json_file)
    user = data['user'].get("name")
    fileName = (user + "_Anime-Planet_Anime-Data_" + str(time.month) + "-" + str(time.day) + "-" + str(time.year) + ").txt")
    DataPort = open(fileName, "a+")
    DataPort.write("====[Anime-Planet Anime Data]====")
    DataPort.write("\nName: " + user)
    DataPort.write("\nExport Date: " + data['export'].get("date"))
    DataPort.write("\nExport Version: " + data['export'].get("version"))
    DataPort.write("\n=================================")
    for anime in data['entries']:
        DataPort.write("\n---------------------------------")
        try:
            DataPort.write('\nName:      ' + str(anime['name']))
        except UnicodeEncodeError:
            problemString = str(anime['name'])
            newName = ""
            for character in problemString:
                if character.isalnum():
                    newName += character
                else:
                    newName += "*"
            DataPort.write('\nName:      ' + str(newName))
        DataPort.write('\nStatus:    ' + str(anime['status']))
        DataPort.write('\nStarted:   ' + str(anime['started']))
        DataPort.write('\nCompleted: ' + str(anime['completed']))
        DataPort.write('\nRating:    ' + str(anime['rating']))
        DataPort.write('\nTimes:     ' + str(anime['times']))
        DataPort.write('\nEpisodes:  ' + str(anime['eps']))
        count += 1

DataPort.write("\n=================================")
DataPort.write("\nTotal Anime:  " + str(count))
DataPort.write("\nCompleted at: " + str(time.month) + "/" + str(time.day) + "/" + str(time.year) + " (" + str(time.hour) + ":" + str(time.minute) + ")")
DataPort.write("\n=================================")
DataPort.close()
count = 0
print("Data written to new file: " + fileName)
