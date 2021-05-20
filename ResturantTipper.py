#Resturant Tipper
#
#Ask for the bill and print out
#the 15% and 20% tip numbers

bill = input("Hello there, what is the total of the bill?")
bill = int(bill)

tip1 = bill * 0.15
tip2 = bill * 0.2

print("\n15% tip would be $" + str(tip1))
print("\n20% tip would be $" + str(tip2))

input("\n\nPress enter to exit.")