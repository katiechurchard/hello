
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
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
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


def get_random_word():
    return WORDLIST[random.randint(0, len(WORDLIST))]


def main():
    random.seed(time.time())
    print("Random word: " + get_random_word())
    # print(HANGMAN_TITLE)


if __name__ == '__main__':
    main()
