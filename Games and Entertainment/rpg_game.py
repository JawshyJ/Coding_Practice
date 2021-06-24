# 6/23/2021 - RPG Game
# A game where a user will have an inventory and can make purchases and sales or take on quests.
# # [Tasks]
# # Add general game functions (Generate Quest / Generate Enemies)
# # Add character customization
# # Add economy / rewards
# # For events that occur in 'x' amount of days, add an (!) alert system next to dialogue options where relevant.

import random
import time
import sys

user_input = ""

# User Info
inventory = []
health = 100
armor = 0
coins = 0

# User Stats
coins_spent = 0
quests_completed = 0
enemies_slain = 0

# Game Settings
game_active = True
days_elapsed = 0


def generateEnemy():
    print("Generating Enemy...")


def generateQuest(difficulty):
    print("Generating Quest...")


test_enemy_health = 100

while game_active is True:
    days_elapsed += 1  # Move this statement somewhere else later, to let players make multiple stops in a day
    while True:
        try:
            print("[Day " + str(days_elapsed) + "]")
            user_input = input("What would you like to do? (type a letter to proceed)\n"
                               "[A] - Go Home (View Stats)\n"
                               "[B] - Visit the market (Buy/Sell Goods)\n"
                               "[C] - Visit the local pub (Accept quests)\n"
                               "[D] - Exit Game\n")  # Save/Auto-Save feature will be implemented later.
        except Exception:
            print("Invalid input.")
        if user_input.lower() == "a":
            print("alpha break")
            break
        elif user_input.lower() == "b":
            break
        elif user_input.lower() == "c":
            break
        elif user_input.lower() == "d":
            break
        else:
            print("Type a letter: A, B, C, or D")
    if user_input == "a":
        print("Heading home.")
    elif user_input == "b":
        print("Heading to market.")
    elif user_input == "c":
        print("Heading to pub.")
        print("=====[DEMO]=====")
        while test_enemy_health > 0:
            print("You attack the enemy!")
            damage = random.randint(1, 10)
            test_enemy_health -= damage
            print("Enemy Health: " + str(test_enemy_health) + "/100 (-" + str(damage) + ")")
            time.sleep(1)
    elif user_input == "d":
        print("Exiting game.")
        sys.exit(0)
