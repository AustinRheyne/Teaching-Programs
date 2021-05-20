#Hangman Game
#
#The classic game of Hangman. The computer picks a random word
#And the player has to guess it, one letter at a time

import random

HANGMAN = (
"""
--------
|      |
|
|
|
|
|
|
|
--------------
""",
"""
--------
|      |
|      0
|
|
|
|
|
|
--------------
""",
"""
--------
|      |
|      0
|     -+-
|
|
|
|
|
--------------
""",
"""
--------
|      |
|      0
|    /-+-
|
|
|
|
|
--------------
""",
"""
--------
|      |
|      0
|    /-+-/
|
|
|
|
|
--------------
""",
"""
--------
|      |
|      0
|    /-+-/
|      |
|
|
|
|
--------------
""",
"""
--------
|      |
|      0
|    /-+-/
|      |
|      |
|     |
|     |
|
--------------
""",
"""
--------
|      |
|      0
|    /-+-/
|      |
|      |
|     | |
|     | |
|
-------------- 
""")

maxWrong = len(HANGMAN)-1
words = ("OVERUSED", "CALM", "GUAM", "TAFFETA", "PYTHON", "EHAN")
word = random.choice(words)
soFar = "-" * len(word)
wrong = 0
used = []

print("Welcome To Hangman")

while wrong < maxWrong and soFar != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", soFar)
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()
    
    used.append(guess)
    

    if guess in word:
        print("\nYes!", guess, "is in the word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += soFar[i]
        soFar = new
    else:
        print("Sorry,", guess, "is not in the word.")        
        wrong += 1
    

if wrong == maxWrong:
    HANGMAN[wrong]
    print("\nYou've been hanged")
else:
    print("\nYou guessed it!")

print("\nThe word was", word)
input("\n\nPress enter to exit.")