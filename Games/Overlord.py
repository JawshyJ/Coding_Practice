#11/3/2020 - Overlord
# A game where a user takes control of a small military cell during World War III
# Tasks:
## Add Tutorial information
## Add Advisor Customization
## Add enemy calculations?
## Add Strength system
## Perfect combat algorithms

import random

# System Variables
game = True
tutorial = True
userInput = ""

# Game Variables
Day = 0
Honor = 0
Inbox = 0
Soldiers = 0
SpecOps = 0
unitTypes = ["Soldier", "Spec Ops"]
WMDs = ["Nuclear Bomb", "Chemical Strike"]
# Using a nuclear bomb or chemical strike will drastically decrease honor, but it will prevent enemy occupation.
BaseActual = "Damaged Bunker"
BaseType = ["Damaged Bunker", "Campsite"]
BaseCost = [0, 100]

# Currency
Funds = 0
ResearchMaterial = 0

# Customization Variables
MilitaryName = "Locust"
AdvisorName = "Monica"

# ========================================
# All Methods that'll be used in the game.
# ========================================


def Conflict(player, enemy):
    print(str(player) + " " + str(enemy))


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


def Scenarios():
    selection = ["A local town is being attacked by armed rebels. Locals will provide us with resources if we assist."]


# ========================================
# Main Section Below
# ========================================

# Introduction
Soldiers += 50
print("Welcome to the Overlord Mainframe. Per the Imminent Doom protocol, all surviving resources have been allocated "
      "for your use.\nYou currently have " + str(Soldiers) + " soldiers standing by in the staging area.\n")
userInput = input("(press enter to continue)\n")

while tutorial is True:
    userInput = InputCheck("Welcome to Overlord. Would you like to view the tutorial on how to play?", ["[Yes]", "[No]"]
                           , ["yes", "no"])
    if userInput == "yes":
        print("Tutorial not complete.")
        # [Tutorial Notes]
        # 1 Inbox (Wired Funds, Intel Reports, etc.)
        # 2 Dispatch (Primary Op, Spec Ops (VIP Extraction, Intel Collection, Black Ops, etc.))
        # 3 Status (Funds, Soldiers, Regions Controlled, Soldiers Killed, Soldiers Lost, etc.)
        # 4 Requisition / Purchase (Purchase soldiers, spec ops, WMDs)
        # 5 Research & Development
        # 6 Sleep / Pass Time
        # 7 Settings (Might add cheats later)
        # 8 Save & Exit
    elif userInput == "no":
        print("Tutorial ended.")
        tutorial = False
    else:
        print("What the...")

while game is True:
    userInput = InputCheck("-------------------\n[Location:] " + str(MilitaryName) + " Headquarters, " +
                           str(BaseActual) + "\n[War Room] Day: " + str(Day),
                           ["1. [" + str(Inbox) + "] Inbox", "2. Dispatch", "3. Status", "4. Requisition",
                            "5. Research & Development", "6. Sleep / Pass Time", "7. Settings",
                            "8. Exit (Saving not implemented yet)"], ["1", "2", "3", "4", "5", "6", "7", "8"])
    if userInput == "1":
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "2":
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "3":
        print("[Day: " + str(Day) + "]")
        print("Soldiers:       " + str(Soldiers))
        print("Spec Ops Units: " + str(SpecOps))
        print("Total Missions: 0")
        print("Honor:          " + str(Honor))
        print("This part will look much cleaner later.")
        userInput = input("(press enter to continue)\n")
    if userInput == "4":
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "5":
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "6":
        random = random.randint(1, 3)
        if random == 1:
            print("You head to your cot and sleep for the night.") # Depending on the base type, the sleep message changes
        elif random == 2:
            print("You sit back in your chair and smoke for a bit before heading to sleep.")
        elif random == 3:
            print("You step away from your console and read the latest status report before heading to sleep.")
        # Add a sleep method later to add random sleep/wakeup events (ex: night raids, emergencies, etc.)
        Day += 1
        userInput = input("(press enter to continue)\n")
    if userInput == "7":
        print("Currently the only setting available is changing the name of your organization.")
        print("Would you like to change your organization name?")
        userInput = InputCheck("Current Name: " + MilitaryName, ["[Yes]", "[No]"], ["yes", "no"])
        if userInput == "yes":
            MilitaryName = input("Current Organization Name: " + MilitaryName + "\nEnter your organization's new name:\n")
            print("Your organization name is now: " + MilitaryName)
    if userInput == "8":
        print("Exiting.")
        game = False
