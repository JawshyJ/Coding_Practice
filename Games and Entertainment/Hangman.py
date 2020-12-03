# 3/10/2020: Hangman game
## Tasks
### Add 'guess word' feature
### Read data from text file
### Fix issue where game claims the player lost, even though they won

errors = 0
wins = 0
losses = 0
userGuess = " "
userInput = "yes"
word = ""
wordBank = ""
veteran = False

# This function will generate the stand
def generateStand():
    print("      ____")
    print("     |    |")
    if (errors >= 1):
        print("     |    O")
    else:
        print("     |     ")
    if (errors >= 4):
        print("     |   /|\\")
    elif (errors >= 3):
        print("     |   /|")
    elif (errors >= 2):
        print("     |    |")
    else:
        print("     |")
    if (errors >= 6):
        print("     |   / \\")
    elif (errors >= 5):
        print("     |   /")
    else:
        print("     |")
    print("     |")
    print("_____|_____")

# Generates the blank word
def generateWord(word):
    wordHash = list(word)
    for x in range(0, len(word)):
        if word[x] == " ":
            wordHash[x] = " "
        else:
            wordHash[x] = "_ "
    return wordHash

# Checks letters that were already guessed
def checkLetter(letter):
    if (letter.upper() in wordBank):
        return True
    elif (letter.lower() in wordBank):
        return True
    else:
        return False

def verifyLetter(letter):
    if (letter.upper() in wordList):
        return True
    elif(letter.lower() in wordList):
        return True
    else:
        return False

# Fills the successful guess into the blank spot(s)
def solve(guess, cover, word):
    for x in range(0, len(cover)):
        if guess.lower() == word[x].lower():
            if word[x].isupper():
                cover[x] = guess.upper()
            else:
                cover[x] = guess.lower()
    return cover

# Main section
while (userInput == "yes"):
    if (veteran == False and userInput == "yes"):
        while True:
            try:
                userInput = input("Want to play Hangman? ( Yes / No )\n").lower()
            except Exception:
                print("Invalid input.")
            if (userInput == "yes" or userInput == "no"):
                break
            else:
                print("Invalid input.")
    else:
        while True:
            try:
                userInput = input("Want to play again? ( Yes / No )\n").lower()
            except Exception:
                print("Invalid input.")
            if (userInput == "yes" or userInput == "no"):
                break
            else:
                print("Invalid input.")
    if (userInput == "no"):
        print("Thanks for playing! Here are your stats:")
        print("[STATS]")
        print("Wins: " + str(wins) + " || Losses: " + str(losses))
        input("Type 'Enter' to exit")
        break;
    elif (userInput == "yes"):
        word = input("Please enter a word or phrase: \n")
        wordList = list(word)
        wordCover = generateWord(wordList)
        while (word != "".join(wordCover)):
            while True:
                try:
                    userGuess = input("Guess a letter: \n")
                except ValueError:
                    print("Invalid input.")
                    errors += 1
                if (checkLetter(userGuess) == False and len(userGuess) == 1 and verifyLetter(userGuess) == True):
                    wordBank += str(userGuess)
                    wordCover = solve(userGuess, wordCover, wordList)
                    generateStand()
                    print(" ".join(wordCover))
                    " ".join(wordCover)
                    print(userGuess + " is in the phrase!")
                    break
                else:
                    errors += 1
                    generateStand()
                    print(" ".join(wordCover))
                    " ".join(wordCover)
                    if (userGuess != ""):
                        if (len(userGuess) > 1):
                            print("Too many characters")
                        if (checkLetter(userGuess) == True):
                            print("You already guessed '" + str(userGuess) + "'")
                        if (verifyLetter(userGuess) == False):
                            print("Letter is not in the word/phrase")
                            wordBank += str(userGuess)
                        if (len(userGuess) < 1):
                            print("Not enough characters")
                    else:
                        print("Not enough characters")
        if (errors == 6):
            print("\nYou have lost. The word was: " + "".join(word) + "\n")
            break
        generateStand()
        print(" ".join(wordCover))
        print("You've won!")
        veteran = True
