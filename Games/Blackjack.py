# 3/14/2020 Blackjack
# Tasks
## Make the output look neater
## The 'Ace' card should count as either a 1 or a 10.
## Maybe add the option to bet

import random
import time

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

matches = 0
wins = 0
losses = 0
ties = 0

def resetGame():
    global dealNum, userInput, userState, userCards, userCardsActual, userSum, dealerState, dealerCards, dealerCardsActual, dealerSum, hidden
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


def initiateGame():
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
    dealerSum -= values[dealerCards[0]]
    print("(Player Hand:) " + str(userCardsActual) + " - " + str(userSum))
    if hidden is True:
        output = ""
        for i in range(1, len(dealerCardsActual)):
            if i == len(dealerCardsActual)-1:
                output += (dealerCardsActual[i])
            else:
                output += (dealerCardsActual[i] + ", ")
        print("Dealer's hand: (hidden), " + output)
        print("Dealer's sum: " + str(dealerSum))
    else:
        print("(Player Hand:) " + str(userCardsActual) + " - " + str(userSum))
        print("Here's the dealer's hand: " + str(dealerCardsActual))
        print("Dealer's sum: " + str(dealerSum))


def deal(stance):
    global userState, userCards, userCardsActual, userSum, dealerState, dealerCards, dealerCardsActual, dealerSum, hidden
    if stance == "hit":
        userState = random.randint(1, 12)
        userCards.append(userState)
        userCardsActual.append(cards[userState])
        userSum += values[userState]
        print("You were dealt a " + cards[userState])
        print("(Player Hand:) " + str(userCardsActual) + " - " + str(userSum))
        if hidden is True:
            output = ""
            for i in range(1, len(dealerCardsActual)):
                if i == len(dealerCardsActual)-1:
                    output += dealerCardsActual[i]
                else:
                    output += (dealerCardsActual[i] + ", ")
            print("Dealer's hand: (hidden), " + output)
            print("Dealer's sum: " + str(dealerSum))
        else:
            print("(Player Hand:) " + str(userCardsActual) + " - " + str(userSum))
            print("(Dealer Hand:) " + str(dealerCardsActual) + " - " + str(dealerSum))
    else:
        hidden = False
        print("The dealer has revealed their hidden card: " + str(dealerCardsActual[0]))
        dealerSum += values[dealerCards[0]]
        print("(Player Hand:) " + str(userCardsActual) + " - " + str(userSum))
        print("(Dealer Hand:) " + str(dealerCardsActual) + " - " + str(dealerSum))
        while dealerSum <= userSum:
            print("\n------(Dealer is hitting...)------\n")
            time.sleep(2)
            dealerHit()


def dealerHit():
    global dealerState, dealerCards, dealerCardsActual, dealerSum
    dealerState = random.randint(1, 12)
    dealerCards.append(dealerState)
    dealerCardsActual.append(cards[dealerState])
    dealerSum += values[dealerState]
    print("Dealer received a " + str(dealerState))
    print("(Dealer Hand:) " + str(dealerCardsActual) + " - " + str(dealerSum))

def winCheck():
    global matches, wins, losses, ties
    if dealerSum == 21:
        print("\n===[Dealer has Blackjack, you lost.]===")
        losses += 1
        return "break"
    if userSum == 21:
        while dealerSum < userSum:
            print("\n------(Dealer is hitting...)------\n")
            time.sleep(2)
            dealerHit()
        if dealerSum != 21:
            print("\n===[You got Blackjack!, you've won!]===")
            wins += 1
            return "break"
        else:
            print("\n===[It's a push, both parties tied.]===")
            ties += 1
            return "break"
    if userSum > 21:
        print("\n=====[You've busted, dealer wins.]=====")
        losses += 1
        return "break"
    if dealerSum > 21:
        print("\n=======[Dealer busted, you win!]=======")
        wins += 1
        return "break"

while userInput == "yes":
    while True:
        if matches == 0:
            userInput = input("Want to play a game of BlackJack? ( Yes / No )\n").lower()
        else:
            userInput = input("Want to play again?( Yes / No )\n").lower()
        if userInput == "yes" or userInput == "no":
            break
        else:
            print("Invalid input.")
    if userInput == "yes":
        initiateGame()
    else:
        print("Thanks for playing. Wins, Losses, and Ties will be available as statistics in a later version.")
        break
    while True:
        if winCheck() == "break":
            print("(Player Hand:) " + str(userCardsActual) + " - " + str(userSum))
            print("(Dealer Hand:) " + str(dealerCardsActual) + " - " + str(dealerSum))
            time.sleep(1)
            break
        while True:
            userInput = input("Hit or Stand?\n").lower()
            if userInput == "hit" or userInput == "stand":
                dealNum += 1
                break
            else:
                print("Invalid Input (" + str(userInput) + ")")
        if userInput == "hit":
            deal("hit")
        else:
            deal("stand")
    print("==============[Game Over]==============")
    matches += 1
    userInput = "yes"
    print("Matches: " + str(matches))
    print("Wins:    " + str(wins))
    print("Losses:  " + str(losses))
    print("Ties:    " + str(ties))
    if wins > 0 and losses > 0:
        print("(W/L Ratio:) " + str(wins) + ":" + str(losses) + " (" + str(round((wins / losses) * 100, 2)) + "%)")
    else:
        print("(W/L Ratio:) " + str(wins) + ":" + str(losses))
    resetGame()
