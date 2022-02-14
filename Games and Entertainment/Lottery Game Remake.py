# 11/7/2020 - Lottery Game Remake
# Program generates a random number between 1 and 20. The user has to guess which number it is.

import random

def CheckInput(guess, actual):
    if guess == actual:
        return True
    else:
        return False

MysteryNumber = random.randint(1, 20)
userInput = 0
guesses = 0
Won = False

while guesses < 3:
    userInput = int(input("Guess a number 1 - 20. (" + str(3 - guesses) + " attempt(s) left)\n"))
    if CheckInput(userInput, MysteryNumber) is True:
        print("You guessed the correct number. You've won!")
        Won = True
        break
    else:
        guesses += 1
        if guesses == 0:
            break
        else:
            print("You've guessed the wrong number. Try again.")
            if userInput < MysteryNumber:
                print("(The number is higher)")
            else:
                print("(The number is lower)")

if Won is False:
    print("You lost, the number was: " + str(MysteryNumber))
