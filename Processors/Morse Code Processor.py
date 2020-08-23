# 8/22/2020 Morse Code Processor
# This program will either encode or decode plaintext/morse codes, depending on the user's choice.
# Tasks:
## Fix the Parenthesis issue
## Add a guide to let the user know what each character translates to

import sys

letterDecode = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]
letterEncode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
numberDecode = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numberEncode = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
symbolDecode = [".", ",", ":", "?", "'", "-", "/", "(", ")", '"']
symbolEncode = [".-.-.-", "--..--", "---...", "..--..", ".----.", "-....-", "-..-.", "-.--.", "-.--.-", '.-..-.']


userInput = "null"


def decode(string):
    tempString = string.split()
    decodedString = ""
    for i in range(len(tempString)):
        if tempString[i] == "/":
            decodedString += " "
        elif tempString[i] in letterEncode:
            print(string[i])
            decodedString += letterDecode[letterEncode.index(tempString[i])]
        elif tempString[i] in numberEncode:
            print(string[i])
            decodedString += numberDecode[numberEncode.index(tempString[i])]
        elif tempString[i] in symbolEncode:
            print(string[i])
            decodedString += symbolDecode[symbolEncode.index(tempString[i])]
        else:
            print("Error")
    return decodedString


def encode(string):
    encodedString = ""
    for i in range(len(string)):
        if string[i] == " ":
            encodedString += " / "
        elif string[i].isalpha() is True:
            encodedString += letterEncode[letterDecode.index(string[i].upper())] + " "
        elif string[i] in numberDecode:
            encodedString += numberEncode[numberDecode.index(string[i])] + " "
        elif string[i] in symbolDecode:
            encodedString += symbolEncode[symbolDecode.index(string[i])] + " "
    return encodedString


while True:
    while True:
        try:
            userInput = input("Type 'Encode' / 'Decode' or 'Exit'\n")
        except ValueError:
            print("huh")
        if userInput.lower() == "encode" or userInput.lower() == "decode" or userInput.lower() == "exit":
            break
        else:
            print("Invalid input.")
    if userInput.lower() == "encode":
        userInput = input("Enter a string to encode.\n")
        print(encode(userInput))
    elif userInput.lower() == "decode":
        userInput = input("Enter a string to decode.\n")
        print(decode(userInput))
    else:
        sys.exit()
