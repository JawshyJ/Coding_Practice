#11/3/2020 - Overlord
# A game where a user takes control of a small military cell during World War III

game = True
bankYN = ["yes", "no"]

userInput = ""

def InputCheck(phrase, listName):
    while True:
        text = input(phrase)
        if text.lower() in listName:
            return text


while game is True:
    print("Welcome to Overlord.")
    userInput = InputCheck("Type yes or no\n", bankYN)
    game = False
