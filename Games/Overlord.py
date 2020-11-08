#11/3/2020 - Overlord
# A game where a user takes control of a small military cell during World War III

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
WMDs = ["Nuclear Bomb", "Chemical Strike"] # Using a nuclear bomb or chemical strike will drastically decrease honor,
BaseStatus = ["Bunker Site", ""]           # but it will prevent enemy occupation.
BaseStatus = [0, 100]

# Currency
Funds = 0
ResearchMaterial = 0

# Customization Variables
MilitaryName = "Cicada"
AdvisorName = "Monica"

# ========================================
# All Methods that'll be used in the game.
# ========================================
def Conflict(player, enemy):
    print(str(player) + " " + str(enemy))


def InputCheck(phrase, optionlist, options):
    string = (phrase + "\n-----[OPTIONS]-----\n")
    for i in range(len(optionlist)):
        string += ("[" + str(optionlist[i]) + "]\n")
    while True:
        text = input(string)
        if text.lower() in options:
            return text
            options.clear()


def Scenarios():
    selection = ["A local village is being attacked by pirates. Locals will provide us with resources"]


# ========================================
# Main Section Below
# ========================================

# Introduction
Soldiers += 50
print("Welcome to the Overlord Mainframe. Per the Imminent Doom protocol, all surviving resources have been allocated "
      "for your use.\nYou currently have " + str(Soldiers) + " soldiers standing by in the staging area.\n")
userInput = input("(press enter to continue)\n")

while tutorial is True:
    userInput = InputCheck("Welcome to Overlord. Would you like to view the tutorial on how to play?", ["Yes", "No"], ["yes", "no"])
    if userInput == "yes":
        print("Tutorial not complete.")
        # Inbox (Wired Funds, Intel Reports, etc.)
        # Dispatch (Primary Op, Spec Ops (VIP Extraction, Intel Collection, Black Ops, etc.))
        # Status (Funds, Soldiers, Regions Controlled, Soldiers Killed, Soldiers Lost, etc.)
        # Requisition / Purchase (Purchase soldiers, spec ops, WMDs)
        # Research & Development
        # Sleep / Pass Time
        # Save & Exit
    elif userInput == "no":
        print("Tutorial ended.")
        tutorial = False
    else:
        print("What the...")

while game is True:
    print("[Sample Menu]")
    userInput = InputCheck("[War Room] Day: " + str(Day), ["(" + str(Inbox) + ") Inbox", "Status"])
    game = False
