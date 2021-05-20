#Word Jumble
#
#The computer picks a random word and "jumbles" it
#The player has to guess the word


import random

#Create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")

#Pick one word randomly from the sequence
word = random.choice(WORDS)

#Create a variable to use as a check for the player
correct = word

#Create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#Begin the game
print(
'''
            Welcome to Word Jumble!
        
        Unscramble the letters to make a word.
     (Press the enter key at any moment to quit.)
'''
)

print("The jumble is:", jumble)

#Allow to player to guess
guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("\nYour guess: ")

#Once the player has won
if guess == correct:
    print("That's it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")