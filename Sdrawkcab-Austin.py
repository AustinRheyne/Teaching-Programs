#Backwords Game
#
#Asks a player for a word
#And outputs it backwords

word = input("What word would you like reversed? ")

backWord = ""
while word:
    pos = (len(word)-1)
    backWord += word[pos]
    word = word[:pos]
 
print("Your reversed word is: ", backWord)