# A guest cant make it! start by using the code from the guest-list program
dinnerList = ["George Washington", "Jim Carrey", "Spongebob"]

print(dinnerList[0] + ", You are invited to a dinner party at my house Thursday night. Hope to see you there!")
print(dinnerList[1] + ", You are invited to a dinner party at my house Thursday night. Hope to see you there!")
print(dinnerList[2] + ", You are invited to a dinner party at my house Thursday night. Hope to see you there!")

# Next print out who cant make it
print(dinnerList[1] + ", is unable to make the dinner party!")

# Replace that guest with a new guest
del dinnerList[1]
dinnerList.append("Patrick")
print("\n")

print(dinnerList[0] + ", You are invited to a dinner party at my house Thursday night. Hope to see you there!")
print(dinnerList[1] + ", You are invited to a dinner party at my house Thursday night. Hope to see you there!")
print(dinnerList[2] + ", You are invited to a dinner party at my house Thursday night. Hope to see you there!")