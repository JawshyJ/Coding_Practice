# 10/2/2020 - CSV Reader (alternate)
# The purpose of this program is to read data from a csv file and to return basic information about it
# Tasks
## Output how many lines and filled cells there are
## Make it so that the program creates a new entry for each header column
## User will be able to attain statistical data, such as: mean, median, mode, etc.
### They'll be able to choose what data they want to interact with
## Find out how to iterate through a class object and ignore the default attributes


### Steps the user will go through
# Build the dataset
# Use tools to analyze numerical sets
## compatible columns will be added to a certain array to show the user they are compatible for that certain measure
## for instance, mode can be applied to strings.


import csv
import datetime
import os
from tkinter import filedialog

name = filedialog.askopenfilename()
currentDirectory = os.path.dirname(os.path.realpath(name))
nameProcessed = os.path.splitext(os.path.basename(name))[0]
time = datetime.datetime.now()


file = open(name, newline='')
reader = csv.reader(file)
header = next(reader)

data = []
dataHeader = []

rowCount = 0
for row in header:
    dataHeader.append(row)
    rowCount += 1
data.append(dataHeader)

colCount = 0
for row in reader:
    rowStack = []
    rowStack.clear()
    colCount += 1
    for column in row:
        rowStack.append(column)
    data.append(rowStack)

for i in range(0, colCount):
    for j in range(0, rowCount):
        if i == 0 and j != rowCount-1:
            print("%15s" % data[i][j], end=" ")
        elif j == rowCount-1:
            print("%15s" % data[i][j], end="\n")
        else:
            print("%15s" % data[i][j], end=" ")

