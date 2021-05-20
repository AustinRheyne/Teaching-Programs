import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

#Set __init__ values
theNumber = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

#Guess loop 
while guess != theNumber:
    if guess > theNumber:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("\nTake a guess: "))
    tries += 1   


#Player guesses the number
print("Congratulations! You guessed my number! The number was", str(theNumber))
print("Holy cow, it only took you", str(tries), "tries!\n")

input("\n\nPress the enter key to exit..")