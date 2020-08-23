# 8/4/2020 Anime Plane Manga Export Processor
# The purpose of this program is to process all of the manga data from a JSON file into a neat and organized text file.

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

class mangaObject:
    def __init__(self, mname, status, started, completed, rating, volume, chapter):
        self.name = mname
        self.status = status
        self.started = started
        self.completed = completed
        self.rating = rating
        self.volume = volume
        self.chapter = chapter

mangaList = []

with open(name) as json_file:
    data = json.load(json_file)
    user = data['user'].get("name")
    fileName = (" Anime-Planet user_" + user + " Manga Data (" + str(time.month) + "-" + str(time.day) + "-" + str(time.year) + ").txt")
    DataPort = open(os.path.join(currentDirectory, fileName), "w")
    DataPort.write("=========[Anime-Planet Manga Data]=========")
    DataPort.write("\nName: " + user)
    DataPort.write("\nExport Date: " + data['export'].get("date"))
    DataPort.write("\nExport Version: " + data['export'].get("version"))
    DataPort.write("\nCompatible Versions: (0.1a) as of " + versionDate)
    DataPort.write("\n===========================================")
    for manga in data['entries']:
        tempName = str(manga['name'])
        tempStatus = str(manga['status'])
        tempStarted = str(manga['completed'])
        tempCompleted = str(manga['completed'])
        tempRating = str(manga['rating'])
        tempVolume = str(manga['vol'])
        tempChapter = str(manga['ch'])
        tempManga = (mangaObject(tempName, tempStatus, tempStarted, tempCompleted, tempRating, tempVolume, tempChapter))
        mangaList.append(tempManga)
        count += 1
    mangaList = sorted(mangaList, key=operator.attrgetter('name'))
    for obj in mangaList:
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
        DataPort.write('\nVolume:     ' + obj.volume)
        DataPort.write('\nChapter:  ' + obj.chapter)

DataPort.write("\n===========================================")
DataPort.write("\nTotal Manga:  " + str(count))
DataPort.write("\nCompleted at: " + str(time.month) + "/" + str(time.day) + "/" + str(time.year) + " (" + str(time.hour) + ":" + str(time.minute) + ")")
DataPort.write("\n===========================================")
DataPort.close()
count = 0
print("Data written to new file: " + fileName)