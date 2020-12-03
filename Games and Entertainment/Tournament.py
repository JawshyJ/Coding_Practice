# 8/5/2020 Tournament Game

import random

game = True
initialPlayers = []
players = []
scores = []
userInput = ""


def InputCheck(phrase, options):  #My favorite method as of late
    while True:
        text = str(input(phrase)).lower()
        if text in options:
            return text
            phrase = ""
        else:
            print("{Error. Select a valid option.}")

def PrepScores():
    scores.clear()
    for i in range(0, len(players)):
        scores.append(0)


# the user should be able to edit or delete any of them should they choose to do so, and the table will adjust accordingly
# when they are satisfied, they can begin the tournament.
# the program will grab two random values in the players array and ask the user which they prefer and they'll discard the other (perhaps into an alternative array)
# there should also be scoring. The more a value wins, the higher its score. The second array can help check the scores of the previous losses that had potential
# when complete, all values will be printed side-by-side with their scores, like so:
## alpha   - 20
## bravo   - 10
## charlie - 5

print("Welcome to my tournament program. This program should help you set up a simple tournament, \n"
      "or help you choose your favorite out of a list of preferences, ex: favorite game/movie")

while game is True:
    while userInput.lower() != "done":  #For some reason, the program executes, even when there are less than 2 players
        userInput = input("Enter a participant. Type 'Done' when you're finished.\n")
        if userInput.lower() == "done" and len(players) < 2:
            userInput == ""
            print("You need at least two players to start the tournament.")
        if userInput.lower() != "done":
            players.append(userInput)

    while True:
        userInput = InputCheck("Here are your players: \n" + str(', '.join(players)) + "\nTotal Players: " +
                               str(len(players)) + "\nWould you like to make any changes? Type 'Yes' or 'No'\n",
                               ["yes", "no"])
        if userInput == "yes":
            userInput = InputCheck("Would you like to add, delete, or edit a player?\n", ["add", "delete", "edit"])
            if userInput == "add":
                while userInput.lower() != "done":
                    userInput = input("Enter a participant. Type 'Done' when you're finished.\n")
                    if userInput.lower() != "done":
                        players.append(userInput)
            if userInput == "delete":
                while userInput.lower() != "done":
                    print("Select a player to delete. Type 'Done' when finished.")
                    count = 0
                    for i in range(0, len(players)):
                        count += 1
                        print(str(i) + " " + str(players[i]))
                    userInput = input("Select a number next to the player you want to delete or type 'Done'.\n").lower()
                    if userInput != "done" and 0 < int(userInput) < len(players):
                        if len(players) <= 2:
                            print("You need at least two players on the team.")
                            break
                        else:
                            del players[int(userInput)]
            if userInput == "edit":
                while userInput.lower() != "done":
                    print("Select a player to edit. Type 'Done' when finished.")
                    for i in range(0, len(players)):
                        print(str(i + 1) + " " + str(players[i]))
                    userInput = input("Select a number next to the player you want to edit or type 'done'.\n").lower()
                    if userInput != "done" and 0 < int(userInput) < len(players):
                        temp = int(userInput) - 1
                        players[temp]
                        userInput = input(str(players[int(temp)]) + "\nCorrect/Replace the player:\n")
                        players[temp] = userInput
        else:
            random.shuffle(players)
            PrepScores()
            break

    while len(players) != 1:
        a = players[0]
        b = players[1]
        userInput = InputCheck("Select A or B to choose a winner:\n[A] " + str(a) + "\n[B] " + str(b) + "\n",
                               ["a", "b"])
        if userInput == "a":
            print(players)
            del players[1]
            print(players)
        else:
            print(players)
            del players[0]
            print(players)

    print("The tournament is officially over!\nThe winner is: " + str(a))
    userInput = InputCheck("\nWould you like to run another tournament? Type 'Yes' or 'No'\n", ["yes", "no"])
    if userInput == "yes":
        userInput = InputCheck("Would you like to use the same players as before or new players? Type 'Same' or 'New'",
                               ["same", "new"])
        if userInput == "same":
            players.clear()
            players = initialPlayers
            break
        else:
            players.clear()
            break
    else:
        quit()
