# 5/5/2024 - Character Generator
## Generation Order (Per Character)
# User selects anywhere between 1 - 1,000,000 characters to generate.
# Gender
# Race
# Ethnicity
# First Name
    # (Based on Gender (Mostly) and Ethnicity (partially))
# Last Name
    # (Based on Ethnicity (partially))
# Skin Tone
    # (Based mostly on Ethnicity)
# Age
    # (Should mostly average between 20 and 60. min/max of 0 and 100)
# Sexuality
    # (Based on Gender and Age. Sexuality will only apply to characters after a certain age)
# Occupation
    # (Based on Age. 0 - 4 N/A, 4-13 School, 14+ etc.)
# Height
    # (Based on Age)
# Weight
    # (Based on Age, Height)
# Wealth
    # (Based on Age, bias against ages younger than 25, but they still have a chance at high wealth)
# Hair Color
    # (Based on Race, but can be a variety of colors in rare chances)
# Eye Color
    # (Based on Race, but can vary in rare chances)
# Virtue
    # (Based on the 7 heaenly virtues)
# Vice
    # (Based on Age and the 7 deadly sins, only one will be selected for each character. Vice will only be applied to
    # characters above a certain age)
# Morality
    # (Based on the morality chart, high chance of good, modest chance of neutral, and small chance of evil)

import datetime
import math
import os
import random
import sys
from tkinter import filedialog


# Standard Value Declarations
user_input = ""
character_count = 0

# Bias Values
bias_check = False
bias_gender = ["", 0]  # M/F, bias percentage
bias_race = ["", 0]  # Caucasoid, Mongoloid, Negroid (Consider better, more generic names)
bias_age = ["", 0]  # Will be based on age group? or range of ages (min/max)?


class characterObject:
    def __init__(self, gender, race, ethnicity, first_name, last_name, skin_tone, age, sexuality, occupation, height,
                 weight, hair_color, eye_color, virtue, vice, morality):
        self.gender = gender  # M/F
        self.race = race
        self.ethnicity = ethnicity
        self.first_name = first_name
        self.last_name = last_name
        self.skin_tone = skin_tone
        self.age = age
        self.sexuality = sexuality
        self.occupation = occupation
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.virtue = virtue
        self.vice = vice
        self.morality = morality  # (Lawful/Neutral/Chaotic) (Good/Neutral/Evil)

def bias_check():  # Allows users to tweak biases
    bias_check = True
    while True:
        try:
            user_input = input("Welcome to the bias check. Please select a bias:\n(A) Gender\n(B) Race\n(C) Age"
                               "\n(D) - Exit -\n").lower()
        except Exception:
            print("Invalid input.")
        if user_input == "a":
            while True:
                user_input = input("Pick Male or Female (M/F)\n").lower()
                print(user_input)
                if user_input == "m" or user_input == "f":
                    bias_gender[0] = user_input
                    while True:
                        try:
                            user_input = int(input("Enter a whole number 0 - 100% to designate the bias percentage"
                                                   "\n").replace("%", ""))
                        except ValueError:
                            print("Please enter an integer between 1 - 100")
                        else:
                            if user_input > 0 and user_input <= 100:
                                bias_gender[1] = user_input
                                break
                    break
                else:
                    print("Enter 'M' or 'F'")
        elif user_input == "b":
            print("B.")
        elif user_input == "c":
            print("C.")
        elif user_input == "d":
            print("Exiting.")
            break
        else:
            print("Invalid input.")


def bias_calculator(value):
    random_value = random.randint(0, 100)
    if random_value >= 100 - value:
        return True
    else:
        return False


def generate_gender():
    if bias_gender[1] != 0:
        if (bias_calculator(bias_gender[1])) is True:  # If the user's bias succeeds
            if bias_gender[0] == "m":
                return "Male"
            if bias_gender[0] == "f":
                return "Female"
        else:  # If the user's bias fails
            if bias_gender[0] == "m":
                return "Female"
            if bias_gender[0] == "f":
                return "Male"
    else:
        generation = random.randint(0, 1)
        if generation == 1:
            return "Male"
        else:
            return "Female"


def generate_age():
    if bias_age[1] != 0:
        print("Age bias present")
    else:
        return random.randint(0, 100)



def user_interview():  # Primary method
    while True:
        try:
            user_input = input("[Character Generator]\nWould you like to account for any biases? (Yes/No)\n").lower()
            print("input: " + str(user_input))
        except Exception:
            print("Invalid input.")
        else:
            if user_input == "yes":
                bias_check()
            if user_input == "no":
                while True:
                    try:
                        character_count = int(
                            input("How many characters would you like to generate? (1 - 1,000,000)\n").replace(",",
                                                                                                               ""))
                        print("count: " + str(character_count))
                    except Exception:
                        print("Invalid input.")
                    else:
                        for i in range(character_count):
                            print(str(format(i + 1, ",")) + ", " + str(generate_gender()) + ", "
                                  + str(generate_age()))  # ----- TEST CODE
                        break

# USE PYTHON PANDAS. STORE ALL VALUES TO EXCEL ROW? LOOP UNTIL COUNT IS MET.

## SECTIONS
# [x] Gender
# [] Race (In Progress, but need data)
# [] Ethnicity (Need data)
# [] First Name (Need data)
# [] Last Name (Need data)
# [] Skin Tone (Need data)
# [] Age (Should be easy)
# [] Sexuality (U: Straight/Asexual, M: Gay, F: Lesbian)
# [] Occupation (Based on age, find list of many occupations)
# [] Height (Varies)
# [] Weight (Varies on age and height)
# [] Wealth
# [] Hair Color
# [] Eye Color
# [] Virtue
# [] Vice
# [] Morality



# user_interview()

# ----- TEMPORARY SECTION
user_interview()
# generate_gender()


