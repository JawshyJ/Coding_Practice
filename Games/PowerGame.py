# 7/24/2020: Power Game
# Tasks
## A leaderboard will be created later on to store the previous lost games
## A statistics collector will keep track of how many games were lost and provide percentages of win probability
# Purpose
## The purpose of this game is to mess around with probability in order to calculate how often a user can get lucky based upon equal or overwhelming chances
# Rules
## The player will 'roll' a hypothetical die along with the opponent. Every 5th roll will be considered a 'boss' round. The opponent has a double the likelihood of attaining a higher number than the player. If the player wins, then their pool of possible numbers doubles as well.

import random

power = 6
potentialPower = 6
rolls = 0
finalScore = 0
home = 0
defense = 0

while True:
    rolls += 1
    print("=====[Roll # " + str(rolls) + "]=====")
    if rolls % 5 == 0 and rolls >= 5:
        print("=====[BOSS ROLL]=====")
        potentialPower *= 2
        home = random.randint(1, power)
        defense = random.randint(1, potentialPower)
        print("Home Roll: " + str(home))
        print("Defense Roll: " + str(defense))
        if home >= defense:
            print("[SYSTEM] Boss roll won")
            print("[SYSTEM] Power increased from " + str(power) + " to " + str(power*2))
            power *= 2
        else:
            print("[SYSTEM] Boss roll lost")
            finalScore = power
            break
    else:
        home = random.randint(1, power)
        defense = random.randint(1, potentialPower)
        print("Home: " + str(home))
        print("Defense: " + str(defense))
        if home >= defense:
            print("[SYSTEM] Roll " + str(rolls) + " won")
            finalScore = power
        else:
            print("[SYSTEM] User lost at Roll # " + str(rolls))
            break

print("[SYSTEM] Final Score: " + str(finalScore))