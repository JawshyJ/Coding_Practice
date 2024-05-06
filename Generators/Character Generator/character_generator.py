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

# Bias Values
bias_gender = ["", 0.0] # M/F, bias percentage
bias_race = ["", 0.0] #
bias_age = ["", 0.0]

class characterObject:
    def __init__(self, gender, race, ethnicity, first_name, last_name, skin_tone, age, sexuality, occupation, height,
                 weight, hair_color, eye_color, virtue, vice, morality):
        self.gender = gender
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
        self.morality = morality


def user_interview:






