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
    selection = ["A local town is being attacked by armed rebels. Locals will provide us with resources if we assist.",
                 "A local militia is prepping for an attack against a terrorist outpost. If we assist, they'll provide "
                 "us with raw materials.", ""]
    specOps = [""]
    blackOps = ["One of our allies has acquired a motherlode of intel, but they don't intend on sharing. If we send in "
                "a cover team, we can download and acquire all of it. Though if we're caught, it could be problematic.",
                "We've located the residential home of an enemy general. If we raid the property, we'll have leverage "
                "over the general. If we fail, even our allies will condemn our actions."]
    return random.randint(0, len(selection)-1)


# ========================================
# Main Section Below
# ========================================

# Tutorial
Funds += 500
Soldiers += 50
print("Welcome to the Overlord Mainframe. Per the Doomsday protocol, all surviving resources have been allocated for "
      "your use.\nYou currently have " + str(Soldiers) + " soldiers standing by in the staging area.\n")
userInput = input("(press enter to continue)\n")

while tutorial is True:
    userInput = InputCheck("Welcome to Overlord. Would you like to view the tutorial on how to play?", ["[Yes]", "[No]"]
                           , ["yes", "no"])
    if userInput == "yes":
        while tutorial is True:
            userInput = InputCheck("This game is played via a menu identical to the one below. Select a menu option \n"
                                   "to learn more about it.",
                                   ["1. Inbox", "2. Dispatch", "3. Status", "4. Requisition", "5. Research &"
                                                                                              "Development",
                                    "6. Sleep/Pass Time", "7. Settings", "8. Save & Exit", "9. Exit Tutorial"],
                                   ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            if userInput == "1":  # Inbox option
                print("1. [Inbox]\n"
                      "The inbox is where you'll receive messages from your assistant and associates. Occasionally,\n"
                      "you'll even receive wired payments and intel reports from your allies and interested parties \n"
                      "based on your honor. Some emails will require a response, which may result in beneficial or \n"
                      "detrimental consequences.")
                userInput = input("(press enter to continue)\n")
            if userInput == "2":  # Dispatch option
                print("2. [Dispatch]\n"
                      "The dispatch screen consists of primary ops and special ops. Primary operations are your main \n"
                      "source of income and growth. They consist purely of using soldiers to carry out missions. \n"
                      "Special operations consist of extracting VIPs, intel, and in some cases: black ops. Black \n"
                      "operations involve performing ethically questionable tasks in order to achieve high rewards.\n"
                      "If you succeed, the reward will greatly offset the cost. If you fail, you'll lose honor.")
                userInput = input("(press enter to continue)\n")
            if userInput == "3":  # Status option
                print("3. [Status]\n"
                      "This is the most important screen of the game. This is where you'll manage your organization. \n"
                      "The status screen will display your funds, soldiers, total kills, total losses, the regions \n"
                      "you control, etc. Use this information to ensure that your organization remains effective.")
                userInput = input("(press enter to continue)\n")
            if userInput == "4":  # Requisition option
                print("4. [Requisition]\n"
                      "In this screen, you'll be able to purchase soldiers, spec ops teams, and various other \n"
                      "equipment, such as WMDs. Beware, if you purchase a WMD, your honor will go down and you may \n"
                      "receive messages pressuring you to relinquish or disarm them. If you choose to disarm them, \n"
                      "you can do so in the 'Research & Development' screen.")
                userInput = input("(press enter to continue)\n")
            if userInput == "5":  # Research & Development option
                print("5. [Research & Development]\n"
                      "Research & Development is where you can begin projects which will allow you to build certain \n"
                      "items without having to purchase them. You'll have to wait a few days, but it's still cheaper \n"
                      "than using your funds. You can eventually disarm nuclear weapons if you complete enough \n"
                      "projects.")
                userInput = input("(press enter to continue)\n")
            if userInput == "6":  # Sleep/Pass Time option
                print("6. [Sleep/Pass Time]\n"
                      "Sleeping will pass time, allowing you to progress through missions and research projects much \n"
                      "quicker. In the case of an emergency, you may be woken up in order to respond.")
                # [REMOVE AFTER IMPLEMENTATION]
                # A base can get attacked and the player can choose whether to evacuate or not
                # (if they evacuate, they lose a large portion of their materials and intel, but their org survives)
                # (if they stay and they're strong enough, they lose nothing but a few defending soldiers)
                # (If they stay and aren't strong enough, they'll lose all of their defending soldiers, all of their
                # # intel, and all of their materials. If they have a lot more soldiers not at base, then eventually
                # # they'll rescue the overlord and their team. If not, the entire organization is destroyed.)
                userInput = input("(press enter to continue)\n")
            if userInput == "7":  # Settings option
                print("7. [Settings]\n"
                      "In this screen, you can adjust various game variables, customize your organization, and \n"
                      "configure the save location for the game.")
                userInput = input("(press enter to continue)\n")
            if userInput == "8":  # Save & Exit option
                print("9. [Save & Exit]\n"
                      "This option allows the user to save their progress and exit")
                # Saving not yet implemented, but all variables will be saved to a file every time the user sleeps.
                # A load system will be implemented later. Users will be able to save where they want.
                userInput = input("(press enter to continue)\n")
            if userInput == "9":  # Exit Tutorial option
                tutorial = False
    elif userInput == "no":
        print("Tutorial ended.")
        tutorial = False
    else:
        print("(TUTORIAL ERROR) What the...")

# Main portion
while game is True:
    userInput = InputCheck("-------------------\n[Location:] " + str(MilitaryName) + " Headquarters, " +
                           str(BaseActual) + "\n[War Room] Day: " + str(Day),
                           ["1. [" + str(Inbox) + "] Inbox", "2. Dispatch", "3. Status", "4. Requisition",
                            "5. Research & Development", "6. Sleep / Pass Time", "7. Settings",
                            "8. Exit (Saving not implemented yet)"], ["1", "2", "3", "4", "5", "6", "7", "8"])
    if userInput == "1":  # Inbox option
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "2":  # Dispatch option
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "3":  # Status option
        print("[Day: " + str(Day) + "]")
        print("Soldiers:       " + str(Soldiers))
        print("Spec Ops Units: " + str(SpecOps))
        print("Total Missions: 0")
        print("Honor:          " + str(Honor))
        print("This part will look much cleaner later.")
        userInput = input("(press enter to continue)\n")
    if userInput == "4":  # Requisition option
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "5":  # Research & Development option
        userInput = input("Currently unavailable.\n(press enter to continue)\n")
    if userInput == "6":  # Sleep / Pass Time option
        random = random.randint(1, 3)
        if random == 1:
            print("You head to your cot and sleep for the night.")  # Depending on the base type, the sleep message changes
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
