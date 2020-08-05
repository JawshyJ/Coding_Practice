# 8/4/2020 Anime Plane Manga Export Processor
# The purpose of this program is to process all of the manga from a JSON file into a neat and organized text file.

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
    fileName = (user + "_Anime-Planet_Manga-Data_" + str(time.month) + "-" + str(time.day) + "-" + str(time.year) + ").txt")
    DataPort = open(fileName, "a+")
    DataPort.write("====[Anime-Planet Manga Data]====")
    DataPort.write("\nName: " + user)
    DataPort.write("\nExport Date: " + data['export'].get("date"))
    DataPort.write("\nExport Version: " + data['export'].get("version"))
    DataPort.write("\n=================================")
    for p in data['entries']:
        DataPort.write("\n---------------------------------")
        DataPort.write('\nName:      ' + p['name'])
        DataPort.write('\nStatus:    ' + p['status'])
        DataPort.write('\nStarted:   ' + str(p['started']))
        DataPort.write('\nCompleted: ' + str(p['completed']))
        DataPort.write('\nRating:    ' + str(p['rating']))
        DataPort.write('\nVolume:    ' + str(p['vol']))
        DataPort.write('\nChapter:   ' + str(p['ch']))
        count += 1

DataPort.write("\n=================================")
DataPort.write("\nTotal Manga:  " + str(count))
DataPort.write("\nCompleted at: " + str(time.month) + "/" + str(time.day) + "/" + str(time.year) + " (" + str(time.hour) + ":" + str(time.minute) + ")")
DataPort.write("\n=================================")
DataPort.close()
count = 0
print("Data written to new file: " + fileName)
