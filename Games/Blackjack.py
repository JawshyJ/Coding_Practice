# 3/14/2020 Blackjack
# Tasks
## Make a method that deals two cards to the player for the first deal then a single card for all subsequent deals
## Make sure that if a user stands or hits, the deal method acts accordingly
## Make sure the win condition is put into place. Maybe collect wins, losses, and ties for statistical purposes.
## Hide the dealer's first card until it's time to reveal (the user
## Maybe add the option to bet

import random

minimum = 2
maximum = 500
current = 100

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealNum = 0
userInput = "yes"
userState = 0
userCards = []
userCardsActual = []
userSum = 0
dealerState = 0
dealerCards = []
dealerCardsActual = []
dealerSum = 0
hidden = True


def initiateGame(): # - Finish this to deal the first two cards for the user and the two cards for the dealer (one of the dealer cards is hidden)
    global userState, userCards, userCardsActual, userSum, dealerState, dealerCards, dealerCardsActual, dealerSum, hidden
    for i in range(0, 2):
        userState = random.randint(1, 12)
        userCards.append(userState)
        userCardsActual.append(cards[userState])
        userSum += values[userState]
        dealerState = random.randint(1, 12)
        dealerCards.append(dealerState)
        dealerCardsActual.append(cards[dealerState])
        dealerSum += values[dealerState]
    print("Here's your current hand: " + str(userCardsActual))
    print("User Sum: " + str(userSum))
    if hidden is True:
        output = ""
        for i in range(1, len(dealerCardsActual)):
            if i == len(dealerCardsActual)-1:
                output += (dealerCardsActual[i])
            else:
                output += (dealerCardsActual[i] + ", ")
        print("Dealer's hand: " + output)
    else:
        print("Here's the dealer's hand: " + str(dealerCardsActual))


def deal(stance): # - Finish this to make it deal a singular card to the user when they choose to hit
    global userState, userCards, userCardsActual, userSum, dealerState, dealerCards, dealerCardsActual, dealerSum
    if stance == "hit":
        userState = random.randint(1, 12)
        userCards.append(userState)
        userCardsActual.append(cards[userState])
        userSum += values[userState]
        print("You have drawn a: " + cards[userState])
        print("Sum of deck: " + str(userSum))
        print("Cards in deck: " + str(userCardsActual))
        if hidden is True:
            output = ""
            for i in range(1, len(dealerCardsActual)):
                if i == len(dealerCardsActual)-1:
                    output += dealerCardsActual[i]
                else:
                    output += (dealerCardsActual[i] + ", ")
            print("Dealer's hand: " + output)
        else:
            print("Here's the dealer's hand: " + str(dealerCardsActual))

while userInput == "yes":
    while True:
        userInput = input("Want to play a game of BlackJack?\n").lower()
        if userInput == "yes" or userInput == "no":
            break
        else:
            print("Invalid input.")
    while True:
        while True:
            userInput = input("Hit or Stand?\n").lower()
            if userInput == "hit" or userInput == "stand":
                break
            else:
                print("Invalid Input (" + str(userInput) + ")")
        if userInput == "hit":
            print("hit")
            deal("hit")
        else:
            print("stand")
            deal("stand")
