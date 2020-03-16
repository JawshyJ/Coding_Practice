# 03/09/2020: Tic Tac Toe w/ Difficulties
import random

# Initial Values--------------------------------------
Values = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

# Variables we'll be using
userStatus = "yes"
Wins = 0
Ties = 0
Losses = 0
Veteran = False
gameActive = False
userInput = "null"
botInput = 0
Difficulty = "null"

# Generates table-------------------------------------------
def generateTable():
    print("=========")
    print(Values[0] + " | " + Values[1] + " | " + Values[2])
    print("---------")
    print(Values[3] + " | " + Values[4] + " | " + Values[5])
    print("---------")
    print(Values[6] + " | " + Values[7] + " | " + Values[8])
    print("=========")

# Cleans table---------------------
def cleanTable():
    for x in range(0, len(Values)):
        Values[x] = str(x)

# User Win Check-------------------------------------------------------------
def checkUser():
    if (Values[0] == "X" and Values[1] == "X" and Values[2] == "X") or \
            (Values[3] == "X" and Values[4] == "X" and Values[5] == "X") or \
            (Values[6] == "X" and Values[7] == "X" and Values[8] == "X")or \
            (Values[0] == "X" and Values[3] == "X" and Values[6] == "X")or \
            (Values[1] == "X" and Values[4] == "X" and Values[7] == "X")or \
            (Values[2] == "X" and Values[5] == "X" and Values[8] == "X")or \
            (Values[0] == "X" and Values[4] == "X" and Values[8] == "X")or \
            (Values[2] == "X" and Values[4] == "X" and Values[6] == "X"):
        return True
    else:
        return False

# Bot Win Check--------------------------------------------------------------
def checkBot():
    if (Values[0] == "O" and Values[1] == "O" and Values[2] == "O") or \
            (Values[3] == "O" and Values[4] == "O" and Values[5] == "O") or \
            (Values[6] == "O" and Values[7] == "O" and Values[8] == "O")or \
            (Values[0] == "O" and Values[3] == "O" and Values[6] == "O")or \
            (Values[1] == "O" and Values[4] == "O" and Values[7] == "O")or \
            (Values[2] == "O" and Values[5] == "O" and Values[8] == "O")or \
            (Values[0] == "O" and Values[4] == "O" and Values[8] == "O")or \
            (Values[2] == "O" and Values[4] == "O" and Values[6] == "O"):
        return True
    else:
        return False

# Cat's game Check-----------------------------------------------------------
def checkTie():
    if (Values[0] != "0" and Values[1] != "1" and Values[2] != "2" and
            Values[3] != "3" and Values[4] != "4" and Values[5] != "5" and
            Values[6] != "6" and Values[7] != "7" and Values[8] != "8"):
        return True
    else:
        return False

# Randomizer: Generates a random free value
def randomize():
    while True:
        x = random.randint(0,8)
        if (Values[x] != "X" and Values[x] != "O"):
            return x

# Easy Bot: selects a completely random spot
def easyBot():
    return randomize()

# Medium Bot: selects a semi-random spot
def mediumBot():
    if (Values[1] == "X" and Values[2] == "X"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[3] == "X" and Values[6] == "X"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[4] == "X" and Values[8] == "X"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[0] == "X" and Values[2] == "X"):
        if (Values[1] != "X" and Values[1] != "O"):
            return 1
    elif (Values[4] == "X" and Values[7] == "X"):
        if (Values[1] != "X" and Values[1] != "O"):
            return 1
    elif (Values[0] == "X" and Values[1] == "X"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[5] == "X" and Values[8] == "X"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[4] == "X" and Values[6] == "X"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[0] == "X" and Values[6] == "X"):
        if (Values[3] != "X" and Values[3] != "O"):
            return 3
    elif (Values[4] == "X" and Values[5] == "X"):
        if (Values[3] != "X" and Values[3] != "O"):
            return 3
    elif (Values[0] == "X" and Values[8] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[2] == "X" and Values[6] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[1] == "X" and Values[7] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[3] == "X" and Values[5] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[2] == "X" and Values[8] == "X"):
        if (Values[5] != "X" and Values[5] != "O"):
            return 5
    elif (Values[3] == "X" and Values[4] == "X"):
        if (Values[5] != "X" and Values[5] != "O"):
            return 5
    elif (Values[0] == "X" and Values[3] == "X"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[7] == "X" and Values[8] == "X"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[2] == "X" and Values[4] == "X"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[0] == "X" and Values[1] == "X"):
        if (Values[7] != "X" and Values[7] != "O"):
            return 7
    elif (Values[1] == "X" and Values[4] == "X"):
        if (Values[7] != "X" and Values[7] != "O"):
            return 7
    elif (Values[0] == "X" and Values[1] == "X"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[2] == "X" and Values[5] == "X"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[0] == "X" and Values[4] == "X"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    return randomize()

# Hard Bot: selects a predicted spot
def hardBot():
    if (Values[1] == "O" and Values[2] == "O"):  # - Dominate section
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[3] == "O" and Values[6] == "O"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[4] == "O" and Values[8] == "O"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[0] == "O" and Values[2] == "O"):
        if (Values[1] != "X" and Values[1] != "O"):
            return 1
    elif (Values[4] == "O" and Values[7] == "O"):
        if (Values[1] != "X" and Values[1] != "O"):
            return 1
    elif (Values[0] == "O" and Values[1] == "O"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[5] == "O" and Values[8] == "O"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[4] == "O" and Values[6] == "O"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[0] == "O" and Values[6] == "O"):
        if (Values[3] != "X" and Values[3] != "O"):
            return 3
    elif (Values[4] == "O" and Values[5] == "O"):
        if (Values[3] != "X" and Values[3] != "O"):
            return 3
    elif (Values[0] == "O" and Values[8] == "O"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[2] == "O" and Values[6] == "O"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[1] == "O" and Values[7] == "O"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[3] == "O" and Values[5] == "O"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[2] == "O" and Values[8] == "O"):
        if (Values[5] != "X" and Values[5] != "O"):
            return 5
    elif (Values[3] == "O" and Values[4] == "O"):
        if (Values[5] != "X" and Values[5] != "O"):
            return 5
    elif (Values[0] == "O" and Values[3] == "O"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[7] == "O" and Values[8] == "O"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[2] == "O" and Values[4] == "O"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[1] == "O" and Values[4] == "O"):
        if (Values[7] != "X" and Values[7] != "O"):
            return 7
    elif (Values[6] == "O" and Values[8] == "O"):
        if (Values[7] != "X" and Values[7] != "O"):
            return 7
    elif (Values[0] == "O" and Values[1] == "O"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[2] == "O" and Values[5] == "O"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[0] == "O" and Values[4] == "O"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[1] == "X" and Values[2] == "X"):  # -- Denial section
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[3] == "X" and Values[6] == "X"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[4] == "X" and Values[8] == "X"):
        if (Values[0] != "X" and Values[0] != "O"):
            return 0
    elif (Values[0] == "X" and Values[2] == "X"):
        if (Values[1] != "X" and Values[1] != "O"):
            return 1
    elif (Values[4] == "X" and Values[7] == "X"):
        if (Values[1] != "X" and Values[1] != "O"):
            return 1
    elif (Values[0] == "X" and Values[1] == "X"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[5] == "X" and Values[8] == "X"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[4] == "X" and Values[6] == "X"):
        if (Values[2] != "X" and Values[2] != "O"):
            return 2
    elif (Values[0] == "X" and Values[6] == "X"):
        if (Values[3] != "X" and Values[3] != "O"):
            return 3
    elif (Values[4] == "X" and Values[5] == "X"):
        if (Values[3] != "X" and Values[3] != "O"):
            return 3
    elif (Values[0] == "X" and Values[8] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[2] == "X" and Values[6] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[1] == "X" and Values[7] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[3] == "X" and Values[5] == "X"):
        if (Values[4] != "X" and Values[4] != "O"):
            return 4
    elif (Values[2] == "X" and Values[8] == "X"):
        if (Values[5] != "X" and Values[5] != "O"):
            return 5
    elif (Values[3] == "X" and Values[4] == "X"):
        if (Values[5] != "X" and Values[5] != "O"):
            return 5
    elif (Values[0] == "X" and Values[3] == "X"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[7] == "X" and Values[8] == "X"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[2] == "X" and Values[4] == "X"):
        if (Values[6] != "X" and Values[6] != "O"):
            return 6
    elif (Values[0] == "X" and Values[1] == "X"):
        if (Values[7] != "X" and Values[7] != "O"):
            return 7
    elif (Values[1] == "X" and Values[4] == "X"):
        if (Values[7] != "X" and Values[7] != "O"):
            return 7
    elif (Values[0] == "X" and Values[1] == "X"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[2] == "X" and Values[5] == "X"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    elif (Values[0] == "X" and Values[4] == "X"):
        if (Values[8] != "X" and Values[8] != "O"):
            return 8
    return randomize()


# Main Function----------------------------------------------------------------------------
while (userStatus == "yes"):
    if (Veteran == False):
        while True:
            try:
                userStatus = input("Would you like to play tic tac toe? (Yes/No)\n").lower()
            except Exception:
                print("Invalid input.")
            if (userStatus == "yes" or userStatus == "no"):
                break
            else:
                print("Invalid input.")
    else:
        while True:
            try:
                userStatus = input("Play again? (Yes/No)\n").lower()
            except Exception:
                print("Invalid input.")
            if (userStatus != "Yes" or "No"):
                break
            else:
                print("Invalid input.")
    if (userStatus == "yes"):
        gameActive = True
        cleanTable()
        while True:
            try:
                Difficulty = input("Pick a difficulty: ( Easy / Medium / Hard )\n").lower()
            except Exception:
                print("Invalid input.")
            if (Difficulty == "easy" or Difficulty == "medium" or Difficulty == "hard"):
                print("Difficulty: " + Difficulty.capitalize())
                break
            else:
                print("Invalid difficulty.")
    else:
        gameActive = False
    while (gameActive == True):
        generateTable()
        while True:
            try:
                userInput = int(input("Pick an available number\n"))
            except ValueError:
                print("Input was not an integer, try again.")
            if (Values[userInput] != "X" and Values[userInput] != "O"):
                break
            else:
                print(str(userInput) + " is unavailable.")
        Values[userInput] = "X"
        if (checkUser() == True):
            generateTable()
            print("You win!")
            Wins += 1
            gameActive == False
            break
        else:
            if (Difficulty == "easy"):
                if (checkTie() == True):
                    generateTable()
                    print("Cat's game, it's a tie!")
                    Ties += 1
                    gameActive == False
                    break
                botInput = easyBot()
                Values[botInput] = "O"
                print("The bot has selected " + str(botInput))
                if(checkBot() == True):
                    generateTable()
                    print("The bot won!")
                    Losses += 1
                    gameActive == False
                    break
            elif (Difficulty == "medium"):
                if (checkTie() == True):
                    generateTable()
                    print("Cat's game, it's a tie!")
                    Ties += 1
                    gameActive == False
                    break
                botInput = mediumBot()
                Values[botInput] = "O"
                print("The bot has selected " + str(botInput))
                if (checkBot() == True):
                    generateTable()
                    print("The bot won!")
                    Losses += 1
                    gameActive == False
                    break
            elif (Difficulty == "hard"):
                if (checkTie() == True):
                    generateTable()
                    print("Cat's game, it's a tie!")
                    Ties += 1
                    gameActive == False
                    break
                botInput = hardBot()
                Values[botInput] = "O"
                print("The bot has selected " + str(botInput))
                if (checkBot() == True):
                    generateTable()
                    print("The bot won!")
                    Losses += 1
                    gameActive == False
                    break
        Veteran = True  # Changes the veterancy of the user for future replays
else:   # Here, we print the final results for players to review their performance.
    print("========================================")
    print("Thanks for playing! Here are your stats:")
    print("----------------------------------------")
    print("[ Wins: " + str(Wins) + " || Ties: " + str(Ties) + " || Losses: " + str(Losses) + " ]")
    print("========================================")
    input("Press Enter to exit")
