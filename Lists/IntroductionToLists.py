# Create a list of bikes
bicycles = ["Trek", "Cannondale", "Redline", "Specialized"]

# Print out the list
print(bicycles)

# Print the first item from the list
print(bicycles[0])

# Print the last item from the list
print(bicycles[-1])

# Print every item from list
for i in range(4):
    print(bicycles[i])

# Print every item from list ADVANCED
for i in bicycles:
    print(i)

# Print various items from list
print(f"My favorite bike is probably {bicycles[0]}, and my least favorite is {bicycles[-1]}, though I still really like the {bicycles[-1]} bike")

# Add items to the list
bicycles.append("Mountain")
print(bicycles)

# Remove the item that was just added
del bicycles[-1]
print(bicycles)

# Store a removed item as a variable and then call it
payments = [12.65, 17.82, 34.96, 78.24, 4.95]
lastPayment = payments.pop()

print(f"\nMy most recent bill was ${lastPayment} but I payed it this morning")

# Pop a certain item from list
motorcycles = ["honda", "yamaha", "suzuki"]
firstOwned = motorcycles.pop(0)
print(f"\nMy first motorcycle was a {firstOwned.title()}")

# Remove an item from a list by value
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove("ducati")
print(motorcycles)

# Remove an item from a list by value using a variable
tooExpensive = "ducati"
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
motorcycles.remove(tooExpensive)
print(f"\nA {tooExpensive.title()} is too expensive for me.")

