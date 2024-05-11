# 5/5/2024 - Character Generator
## Generation Order (Per Character)
# User selects anywhere between 1 - 1,000,000 characters to generate.
# [X] Gender
# [X] Race
# [] Ethnicity
# [] First Name (Based on Gender (mostly) and Ethnicity (partially))
# [] Last Name (Based on Ethnicity (partially))
# [] Skin Tone (Based mostly on Ethnicity)
# [x] Age (Should mostly average between 20 and 60. min/max of 0 and 100)
# [] Sexuality (Based on Gender and Age. Sexuality will only apply to characters after a certain age)
# [] Occupation (Based on Age. 0 - 4 N/A, 4-13 School, 14+ etc.)
# [] Height (Based on Age)
# [] Weight (Based on Age, Height)
# [] Wealth (Based on Age, bias against ages younger than 25, but they still have a chance at high wealth)
# [] Hair Color (Based on Race, but can be a variety of colors in rare chances)
# [] Eye Color (Based on Race, but can vary in rare chances)
# [] Virtue (Based on the 7 heavenly virtues)
# [] Vice (Based on Age and the 7 deadly sins, only one will be selected for each character. Vice will only be
#          applied to characters above a certain age)
# [x] Morality (Based on the morality chart, high chance of good, modest chance of neutral, and small chance of evil)


import datetime
import math
import os
import random
import sys
from tkinter import filedialog


# Standard values
user_input = ""
character_count = 0

# Bias values
bias_check = False
bias_gender = ["", 0]  # M/F, bias percentage
bias_race = ["", 0]  # Caucasoid, Mongoloid, Negroid (Consider better, more generic names)
bias_age = ["", 0]  # Will be based on age group? or range of ages (min/max)?

# Stat values
male_count = 0
female_count = 0
# average_age = 0


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
                    if user_input == "m":
                        bias_gender[0] == "Male"
                    elif user_input == "f":
                        bias_gender[0] == "Female"
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


def bias_calculator(list):  # Input: ( list[(Item, Weight), ...] )
    weighted_sum = 0
    list.sort(key=lambda sort_list: sort_list[1])  # sorts the list by the values
    for value in range(len(list)):
        weighted_sum += list[value][1]
    roll = random.randint(1, weighted_sum)
    for value in range(len(list)):
        # print("Roll: " + str(roll) + " <=? " + str(list[value][1]) + " (" + str(list[value][0]) + ")")
        if list[value][1] >= roll:
            return list[value][0]
        else:
            roll -= list[value][1]


def generate_gender():
    genders = [["Male", 50], ["Female", 50]]
    if bias_gender[1] != 0:
        if bias_gender[0] == "Male":
            genders[0][1] = bias_gender[1]
            genders[1][1] = 100 - bias_gender[1]
        elif bias_gender[1] == "Female":
            genders[1][1] = bias_gender[1]
            genders[0][1] = 100 - bias_gender[1]
        return bias_calculator(genders)
    else:
        generation = random.randint(0, 1)
        if generation == 1:
            return "Male"
        else:
            return "Female"


def generate_age():  # [TASK] Account for age bias, by showing current bias and allowing user to tweak whichever age
                     # group.
    age_groups = [["Infant", 5], ["Toddler", 10], ["Child", 20], ["Teenager", 40], ["Adult", 80], ["Senior", 30]]
    selected_group = bias_calculator(age_groups)
    if bias_age[1] != 0:
        print("[IN PROGRESS] Age bias present")
    else:
        if selected_group == "Infant":
            return 0
        elif selected_group == "Toddler":
            return random.randint(1, 3)
        elif selected_group == "Child":
            return random.randint(4, 12)
        elif selected_group == "Teenager":
            return random.randint(13, 19)
        elif selected_group == "Adult":
            return random.randint(20, 64)
        elif selected_group == "Senior":
            return random.randint(65, 100)


def generate_race():
    race_list = ("Caucasian", "Asian/Pacific Islander", "African")  # May add 'Other'
    return race_list[random.randint(0, len(race_list) - 1)]


def generate_ethnicity(race):  # TASK - Need Data
    print("- Incomplete -")

def generate_name(first_or_last):  # TASK - Need Data. Names will vary based on gender/ethnicity, to a degree
    print("- Incomplete -")

def generate_skin_tone(ethnicity):  # TASK - Need Data
    print("- Incomplete -")

def generate_sexuality(age, gender):  # TASK - (U: Straight/Asexual, M: Gay, F: Lesbian)
    universal_sexualities = [["Straight", 90], ["Bisexual", 5], ["Asexual", 3]]
    if age >= 14:  # Putting 14 since it seems like most people figure themselves out by high school.
        if gender == "Male":
            universal_sexualities.append(["Gay", 8])
            return bias_calculator(universal_sexualities)
        elif gender == "Female":
            universal_sexualities.append(["Lesbian", 8])
            return bias_calculator(universal_sexualities)
        else:
            return "N/A"
    else:
        return "N/A"
    print("- Incomplete -")

def generate_occupation(age):  # TASK - Need Data, (Based on age, find list of many occupations)
    print("- Incomplete -")


def generate_height(age):  # Varies depending on the age group
    print("- Incomplete -")


def generate_weight(age, height):  # varies on age and height
    print("- Incomplete -")


def generate_wealth(age, occupation):
    print("- Incomplete -")


def generate_hair_color(ethncity):
    print("- Incomplete -")


def generate_eye_color(ethncity):
    print("- Incomplete -")


def generate_virtue(age):
    virtues = [""]  # 7 heavenly virtues
    if age >= 18:
        print("Virtue Test")
    print("- Incomplete -")


def generate_vice(age):
    vices = [""]  # 7 Deadly Sins
    if age >= 18:
        print("Vice Test")
    print("- Incomplete -")


def generate_morality(age):
    moralities = [["Lawful Good", 30], ["Neutral Good", 80], ["Chaotic Good", 15],
                  ["Lawful Neutral", 50], ["True Neutral", 60], ["Chaotic Neutral", 30],
                  ["Lawful Evil", 20], ["Neutral Evil", 15], ["Chaotic Evil", 5]]
    if age >= 13:  # Setting age at
        return bias_calculator(moralities)
    else:
        return "N/A"


def user_interview():  # Primary method
    while True:
        try:
            user_input = input("[Character Generator]\nWould you like to account for any biases? (Yes/No)\n").lower()
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
                            # ----- TEST CODE START
                            temp_gender = generate_gender()
                            temp_age = generate_age()
                            temp_race = generate_race()
                            temp_sexuality = generate_sexuality(temp_age, temp_gender)
                            temp_morality = generate_morality(temp_age)
                            print(str(format(i + 1, ",")) + ": " + str(temp_gender) + ", "
                                  + str(temp_age) + ", " + str(temp_race) + ", " + str(temp_sexuality)
                            + ", " + str(temp_morality))
                            # ----- TEST CODE END
                        try:
                            user_input = input("Would you like to generate another character? (Yes / No)\n").lower()
                        except Exception:
                            print("Invalid input.")
                        else:
                            if user_input == "y" or user_input == "yes":
                                break
                            elif user_input == "n" or user_input == "no":
                                sys.exit(9)
                        break

# USE PYTHON PANDAS. STORE ALL VALUES TO EXCEL ROW? LOOP UNTIL COUNT IS MET.


# user_interview()

# ----- TEMPORARY SECTION
user_interview()
# print(generate_gender())



