# Start with the list of people from the More Guest program
dinnerList = ["Dad", "George Washington", "Jim Carrey", "Austin", "Spongebob", "Bob Ross"]

# It turns out that the table wont arrive in time and only 2 people can come to the party!
# 
# Use pop() to remove guests from the invite list until only 2 are left
# As you remove guests, print out letting them know that they've been uninvited

removedGuest = dinnerList.pop(1)
print(removedGuest + ", you have been uninvited from the dinner party")

removedGuest = dinnerList.pop(1)
print(removedGuest + ", you have been uninvited from the dinner party")

removedGuest = dinnerList.pop(1)
print(removedGuest + ", you have been uninvited from the dinner party")

removedGuest = dinnerList.pop(-1)
print(removedGuest + ", you have been uninvited from the dinner party")

# Next print out a message to the two people left, letting them know that they're still invited
print(dinnerList[0] + ", you're still invited to the party! see you then!")
print(dinnerList[1] + ", you're still invited to the party! see you then!")

# Finally use del to remove the last two party goers from the list and print out the list to make sure its empty
del dinnerList[1]
del dinnerList[0]

print(dinnerList)