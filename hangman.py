
from __future__ import print_function

import random, time


HANGMAN_TITLE = """ _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \.
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
"""

HANGMAN = [
"""








""",
"""







 ____|___""",
"""


     |
     |
     |
     |
     |
 ____|___""",
"""
      _______
     |
     |
     |
     |
     |
     |
 ____|___""",
"""
      _______
     |/
     |
     |
     |
     |
     |
 ____|___""",
"""
      _______
     |/      |
     |
     |
     |
     |
     |
 ____|___""",
"""
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
 ____|___""",
 """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
 ____|___""",
"""
      _______
     |/      |
     |      (_)
     |       |/
     |       |
     |
     |
 ____|___""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
 ____|___""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |        \.
     |
 ____|___""",
"""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \.
     |
 ____|___"""]


WORDLIST = [
    "account",
    "advertisement",
    "attraction",
    "beautiful",
    "competition",
    "development",
    "education",
    "experience",
    "fertile",
    "government",
    "hanging",
    "instrument",
    "knowledge",
    "language",
    "necessary",
    "observation",
    "organization",
    "political",
    "punishment",
    "question",
    "reaction",
    "representative",
    "secretary",
    "sausage",
    "tomorrow",
    "umbrella",
    "yesterday"
]

def check_letter(word, guesses):
    for letter in word:
        if letter not in guesses:
            return False
    print("winner")
    return True


def guess_letter(word, guesses):
    wrong = ""
    print("\n")
    for letter in word:
        if letter in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    for letter in guesses:
        if letter not in word:
            wrong = wrong + letter
    print("\nWrong: ", wrong)
    guess = None
    while guess is None:
        guess = input ("choose a letter ")
        guess = guess.lower().strip()
        if len(guess) > 1 or len(guess) < 1:
            guess = None
    return guess


def get_random_word():
    return WORDLIST[random.randint(0, len(WORDLIST))]


def main():
    random.seed(time.time())
    # variables
    guesses = ""
    wrong_count = 0
    word = get_random_word()
    #
    while not check_letter(word, guesses):
        print(HANGMAN_TITLE)
        print(HANGMAN[wrong_count])
        letter = guess_letter(word, guesses)
        guesses = guesses + letter
        if letter not in word:
            wrong_count = wrong_count + 1
        if wrong_count == len(HANGMAN):
            print("You are dead")
            break


if __name__ == '__main__':
    main()
