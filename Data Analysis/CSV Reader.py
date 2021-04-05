# 9/20/2020 - CSV Reader
# The purpose of this program is to read data from a csv file and to return basic information about it
# Tasks
## Output how many lines and filled cells there are
## Make it so that the program creates a new entry for each header column
## User will be able to attain statistical data, such as: mean, median, mode, etc.
### They'll be able to choose what data they want to interact with


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


class recordClass(object):
    pass


file = open(name, newline='')
reader = csv.reader(file)
header = next(reader)
data = []

record = recordClass()

print(header)
for row in header:
    print("row " + str(row))
    record.row = row
    data.append(record)
    setattr(record, str(row), str(row))
    print(record.__getattribute__(row))



print("Attributes:")
count = 0
for attr in record.__dict__.__iter__():
    if attr in ["__module__", "__dict__", "__weakref__", "__doc__"]: # Bootleg way to ignore these attributes.
        pass
    else:
        print(attr)
        count += 1

for row in reader:
    dataRecord = []
    for column in row:
        dataRecord.append(column)
        print(column)
    print("yea " + ', '.join(dataRecord))
    dataRecord.clear()


print("record " + str(record.Name))


print("Data Record: " + str(dataRecord))

print("Dataset: " + str(data))
for i in range(0, len(data)):
    print(recordClass(i))


for row in reader:
    # row = [ID, Fsize, Housing, Electricity, Water]
    id = str(row[0])

#    data.append(record(id, familySize, housingCost, electricityCost, waterCost))



## Question 1------------------------------------
#print("[Q1] What is the average water expense?")
#sum = 0
#numbers = 0
#for record in data:
    #    sum += record.waterCost
#    numbers += 1

# FileName = filedialog.asksaveasfilename(initialfile=Name + ".txt", filetypes=[("TXT", "*.txt")])

