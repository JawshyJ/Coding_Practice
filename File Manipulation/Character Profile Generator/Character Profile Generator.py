# 4/27/2020 Character Profile Generator
# Tasks
## Make it so that users can choose where the file saves.

import datetime
import math
import os
import random
import sys
from tkinter import filedialog

# Declaring the major variables here
Gender = ""
Name = ""
Age = ""
Height = ""
Weight = ""
Appearance = ""
Role = ""
Strengths = ""
Weaknesses = ""
Summary = "N/A"

userInput = ""
Generate = True
Review = True
Veteran = False
Time = datetime.datetime.now()


def nameGen(gender):
    Names = []
    with open(os.path.join(sys.path[0], "UnisexNames.txt"), "r") as unisex:
        for line in unisex:
            line = line.strip()
            Names.append(line)
    if gender == "Male":
        with open(os.path.join(sys.path[0], "MaleNames.txt"), "r") as male:
            for line in male:
                line = line.strip()
                Names.append(line)
        return Names[random.randint(0, len(Names)-1)]
    if gender == "Female":
        with open(os.path.join(sys.path[0], "FemaleNames.txt"), "r") as female:
            for line in female:
                line = line.strip()
                Names.append(line)
        return Names[random.randint(0, len(Names)-1)]
    Names.clear()


def appGen(gender, age, height, weight):
    colors = ["red", "blue", "green", "hazel", "brown"]
    hair = ["black", "brown", "white", "red", "blue", "purple", "pink"]
    Story = ""
    if gender == "Male":
        Story += "He's "
    else:
        Story += "She's "
    if age <= 10:
        Story += "very young, "
    elif age <= 30:
        Story += "young, "
    elif age <= 55:
        Story += "middle-aged, "
    elif age <= 70:
        Story += "fairly old, "
    else:
        Story += "old, "
    if height <= 64:
        Story += "short, "
    elif height < 72:
        Story += "average height, "
    elif height >= 72:
        Story += "tall, "
    if (int(weight)/(int(height)*(int(height))) * 703) < 18.5:
        Story += "and underweight "
    elif (int(weight)/(int(height)*(int(height))) * 703) < 24.9:
        Story += "and average-weight "
    elif (int(weight)/(int(height)*(int(height))) * 703) < 29.9:
        Story += "and fairly overweight "
    elif (int(weight)/(int(height)*(int(height))) * 703) > 30:
        Story += "and obese "
    chance = str(colors[random.randint(1, len(colors)-1)])
    Story += "with " + chance + " eyes and "
    chance = str(hair[random.randint(1, len(hair)-1)])
    Story += chance + " hair."
    return Story

def roleGen():
    Names = []
    with open(os.path.join(sys.path[0], "Roles.txt"), "r") as unisex:
        for line in unisex:
            line = line.strip()
            Names.append(line)
    return Names[random.randint(0,len(Names)-1)]

def strengthGet():
    Virtues = ["Chastity", "Temperance", "Charity", "Patience", "Kindness", "Humility"]
    return Virtues[random.randint(1, len(Virtues)-1)]

def weaknessGet():
    Vices = ["Lust", "Gluttony", "Greed", "Sloth", "Wrath", "Envy", "Pride"]
    return Vices[random.randint(1, len(Vices) - 1)]


while Generate is True:
    while True:
        try:
            if Veteran is False:
                userInput = input("Would you like to generate a character profile? Yes / No\n")
            else:
                userInput = input("Would you like to generate another character? Yes / No\n")
        except Exception:
            print("Invalid input.")
        if userInput.lower() == "yes":
            break
        elif userInput.lower() == "no":
            Generate = False
            break
        else:
            print("Type 'Yes' or 'No'")
    if Generate is False:
        break
    while True:
        chance = random.randint(1, 2)
        if chance == 1:
            Gender = "Female"
        else:
            Gender = "Male"
        if Gender == "Male":
            Name = nameGen("Male")
        else:
            Name = nameGen("Female")
        Age = random.randint(18, 75)
        chance = random.randint(48, 80)
        Height = (str(math.floor(chance/12)) + "'" + str(chance % 12))
        Weight = str(round(chance * 2))
        Appearance = appGen(Gender, Age, chance, Weight)
        Role = roleGen()
        Strengths = strengthGet()
        Weaknesses = weaknessGet()
        Review = True
        break

    Review = True
    while Review == True:
        print("===========[Character Profile]===========")
        print("1_[Name:] " + Name)
        print("2_[Gender] " + Gender)
        print("3_[Age:] " + str(Age))
        print("4_[Height:] " + Height)
        print("5_[Weight:] " + Weight + " lbs")
        print("6_[Appearance:] " + Appearance)
        print("7_[Role:] " + Role)
        print("8_[Strengths:] " + Strengths)
        print("9_[Weaknesses:] " + Weaknesses)
        print("10_[Summary:] " + Summary)
        print("=========================================")
        try:
            userInput = input("To edit, type a number above or type 'Save'\nIf you'd like to cancel and exit, type 'Exit'\n")
        except Exception:
            print("Invalid input.")
        if userInput == "1":
            Name = input("Enter their new name:\n").capitalize()
        elif userInput == "2":
            while True:
                try:
                    Gender = input("Enter their new gender:\n").lower().capitalize()
                except Exception:
                    print("Invalid input.")
                if Gender.lower() == "male" or Gender.lower() == "female":
                    break
                else:
                    print("Please enter male or female")
        elif userInput == "3":
            if Gender.lower() == "male":
                Age = input("Enter his new age:\n")
            else:
                Age = input("Enter her new age:\n")
        elif userInput == "4":
            Height = input("Enter their new height:\n")
        elif userInput == "5":
            Weight = input("Enter their new weight:\n")
        elif userInput == "6":
            if Gender.lower() == "male":
                Height = input("Enter his new appearance info:\n")
            else:
                Height = input("Enter her new appearance info:\n")
        elif userInput == "7":
            Role = input("What's their role or purpose?\n")
        elif userInput == "8":
            Strengths = input("What are their strengths?\n")
        elif userInput == "9":
            Weaknesses = input("What are their weaknesses?\n")
        elif userInput == "10":
            Summary = input("Write new character summary about " + Name + "\n")
        elif userInput.lower() == "save":
            FileName = filedialog.asksaveasfilename(initialfile=Name + ".txt", filetypes=[("TXT", "*.txt")])
            while True:
                try:
                    Dossier = open(FileName, "a+")
                except FileNotFoundError:
                    print("File Creation Error. Try again.")
                    FileName = filedialog.asksaveasfilename(initialfile=Name + ".txt", filetypes=[("TXT", "*.txt")])
                else:
                    if 1 + 1 is 2:
                        break
            Dossier.write("      [Name:] " + Name)
            Dossier.write("\n    [Gender:] " + Gender)
            Dossier.write("\n       [Age:] " + str(Age))
            Dossier.write("\n    [Height:] " + Height)
            Dossier.write("\n    [Weight:] " + Weight)
            Dossier.write("\n[Appearance:] " + Appearance)
            Dossier.write("\n      [Role:] " + Role)
            Dossier.write("\n [Strengths:] " + Strengths)
            Dossier.write("\n[Weaknesses:] " + Weaknesses)
            Dossier.write("\n   [Summary:] " + Summary)
            Dossier.write("\n[Character generated at: " + str(Time.month) + "/" + str(Time.day) + "/" + str(Time.year) + " (" + str(Time.hour) + ":" + str(Time.minute) + ")]")
            Dossier.close()
            print("Character created at " + str(Time.month) + "/" + str(Time.day) + "/" + str(Time.year) + " (" + str(Time.hour) + ":" + str(Time.minute) + ")")
            Review = False
            Veteran = True
        elif userInput.lower() == "exit":
            Generate = False
            break
