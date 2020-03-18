# 3/17/2020 Character Profile Creator

import datetime

# Declaring the major variables here
Name = ""
Gender = ""
Age = ""
Height = ""
Weight = ""
Appearance = ""
Role = ""
Strengths = ""
Weaknesses = ""
Summary = ""

userInput = ""
Create = True
Review = True
Veteran = False
Time = datetime.datetime.now()

# The main section. It will ask for user data, store them, then allow the user to review and edit the data if necessary.
# If the user is satisfied, then the program will append the data to a text file with the character's name.
while Create == True:
    #print(str(Time.month) + "/" + str(Time.day) + "/" + str(Time.year) + " (" + str(Time.hour) + ":" + str(Time.minute) + ")")
    #print(str(Time)[:16])
    while True:
        try:
            if Veteran == False:
                userInput = input("Would you like to create a character? Yes / No\n")
            else:
                userInput = input("Would you like to create another character? Yes / No\n")
        except Exception:
            print("Invalid input.")
        if userInput.lower() == "yes":
            break
        elif userInput.lower() == "no":
            Create = False
            break
        else:
            print("Type 'Yes' or 'No'")
    if Create == False:
        break
    Name = input("Enter the character's name or nickname:\n").capitalize()
    while True:
        try:
            Gender = input("Enter the character's gender:\n").lower().capitalize()
        except Exception:
            print("Invalid input.")
        if Gender.lower() == "male" or Gender.lower() == "female":
            break
        else:
            print("Please enter male or female")
    Age = input("What's " + Name + "'s age? (or age group):\n")
    if Gender.lower() == "male":
        Height = input("What's his height?\n")
    else:
        Height = input("What's her height?\n")
    if Gender.lower() == "male":
        Weight = input("What's his weight?\n")
    else:
        Weight = input("What's her weight?\n")
    if Gender.lower() == "male":
        Appearance = input("What does he look like? How does he dress?\n")
    else:
        Appearance = input("What does she look like? How does she dress?\n")
    Role = input("What's their role or purpose?\n")
    if Gender.lower() == "male":
        Strengths = input("What are his strengths?\n")
    else:
        Strengths = input("What are her strengths?\n")
    if Gender.lower() == "male":
        Weaknesses = input("What are his weaknesses?\n")
    else:
        Weaknesses = input("What are her weaknesses?\n")
    Summary = input("Write a small character summary about " + Name + ":\n")
    while Review == True:
        try:
            print("===========[Character Profile]===========")
            print("1_[Name:] " + Name)
            print("2_[Gender] " + Gender)
            print("3_[Age:] " + Age)
            print("4_[Height:] " + Height)
            print("5_[Weight:] " + Weight)
            print("6_[Appearance:] " + Appearance)
            print("7_[Role:] " + Role)
            print("8_[Strengths:] " + Strengths)
            print("9_[Weaknesses:] " + Weaknesses)
            print("10_[Summary:] " + Summary)
            print("=========================================")
            userInput = input("To edit, enter a number above or type 'Save'\n")
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
            FileName = Name + ".txt"
            Dossier = open(FileName, "a+")
            Dossier.write("[Name:] " + Name)
            Dossier.write("\n[Gender:] " + Gender)
            Dossier.write("\n[Age:] " + Age)
            Dossier.write("\n[Height:] " + Height)
            Dossier.write("\n[Weight:] " + Weight)
            Dossier.write("\n[Appearance:] " + Appearance)
            Dossier.write("\n[Role:] " + Role)
            Dossier.write("\n[Strengths:] " + Strengths)
            Dossier.write("\n[Weaknesses:] " + Weaknesses)
            Dossier.write("\n[Summary:] " + Summary)
            Dossier.write("\n[Character created at: " + str(Time.month) + "/" + str(Time.day) + "/" + str(Time.year) + " (" + str(Time.hour) + ":" + str(Time.minute) + ")]")
            Dossier.close()
            print("Character created at " + str(Time.month) + "/" + str(Time.day) + "/" + str(Time.year) + " (" + str(Time.hour) + ":" + str(Time.minute) + ")")
            Review = False
            Veteran = True
        else:
            print("Please enter a number 1-10 or type 'Save'")