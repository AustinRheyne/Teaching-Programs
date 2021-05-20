#__init__
maxSticks = 4
minSticks = 1
sticks = 13
currPlayer = 1

instructions = '''
Each player takes turns picking up from 1 to 4 sticks from a pile of 13 sticks.
Whoever picks up the last stick wins.
'''

print("\tWelcome to pickup sticks!\n")
print(instructions)

while sticks > 0:
    grabbedSticks = int(input("Player " + str(currPlayer) + ", please select between 1-4 sticks "))
    while grabbedSticks < 1 or grabbedSticks > 4:
        print("Please choose a number between 1 and 4")
        grabbedSticks = int(input("\nPlayer " + str(currPlayer) + ", please select between 1-4 sticks "))
    print("\nPlayer " + str(currPlayer) + " picked up " + str(grabbedSticks) + " stick(s)")
    
    #Is the player over drawing?
    if sticks - int(grabbedSticks) >= 0:
        sticks -= int(grabbedSticks)

    #Has someone won?
    if sticks != 0:
        currPlayer += 1
    
    #Is the player count too high? 
    if currPlayer > 2:
        currPlayer = 1

print("Player " + str(currPlayer) + " wins!")
input("\n\n\tPress the enter key to exit..")