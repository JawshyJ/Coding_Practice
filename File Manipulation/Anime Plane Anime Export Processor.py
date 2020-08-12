# 8/4/2020 Anime Plane Anime Export Processor
# The purpose of this program is to process all of the anime data from a JSON file into a neat and organized text file.

versionDate = "8/12/2020"

import json
import datetime
import operator
import os
from tkinter import filedialog

name = filedialog.askopenfilename()
currentDirectory = os.path.dirname(os.path.realpath(name))
nameProcessed = os.path.splitext(os.path.basename(name))[0]
count = 0
time = datetime.datetime.now()


class animeObject:
    def __init__(self, aname, status, started, completed, rating, times, eps):
        self.name = aname
        self.status = status
        self.started = started
        self.completed = completed
        self.rating = rating
        self.times = times
        self.eps = eps

animeList = []

with open(name) as json_file:
    data = json.load(json_file)
    user = data['user'].get("name")
    fileName = (user + "_Anime-Planet_Anime-Data_" + str(time.month) + "-" + str(time.day) + "-" + str(time.year) + ").txt")
    DataPort = open(os.path.join(currentDirectory, fileName), "w")
    DataPort.write("=========[Anime-Planet Anime Data]=========")
    DataPort.write("\nName: " + user)
    DataPort.write("\nExport Date: " + data['export'].get("date"))
    DataPort.write("\nExport Version: " + data['export'].get("version"))
    DataPort.write("\nCompatible Versions: (0.1a) as of " + versionDate)
    DataPort.write("\n===========================================")
    for anime in data['entries']:
        tempName = str(anime['name'])
        tempStatus = str(anime['status'])
        tempStarted = str(anime['started'])
        tempCompleted = str(anime['completed'])
        tempRating = str(anime['rating'])
        tempTimes = str(anime['times'])
        tempEps = str(anime['eps'])
        tempAnime = (animeObject(tempName, tempStatus, tempStarted, tempCompleted, tempRating, tempTimes, tempEps))
        animeList.append(tempAnime)
        count += 1
    animeList = sorted(animeList, key=operator.attrgetter('name')) # Sorts the anime alphabetically
    for obj in animeList:
        DataPort.write("\n-------------------------------------------")
        try:
            DataPort.write('\nName:      ' + obj.name)
        except UnicodeEncodeError:
            problemString = obj.name
            newName = ""
            for character in problemString:
                if character.isalnum():
                    newName += character
                else:
                    newName += "*"
            DataPort.write('\nName:      ' + str(newName))
        DataPort.write('\nStatus:    ' + obj.status)
        DataPort.write('\nStarted:   ' + obj.started)
        DataPort.write('\nCompleted: ' + obj.completed)
        DataPort.write('\nRating:    ' + obj.rating)
        DataPort.write('\nTimes:     ' + obj.times)
        DataPort.write('\nEpisodes:  ' + obj.eps)

DataPort.write("\n===========================================")
DataPort.write("\nTotal Anime:  " + str(count))
DataPort.write("\nCompleted at: " + str(time.month) + "/" + str(time.day) + "/" + str(time.year) + " (" + str(time.hour) + ":" + str(time.minute) + ")")
DataPort.write("\n===========================================")
DataPort.close()
count = 0
print("Data written to new file: " + fileName)