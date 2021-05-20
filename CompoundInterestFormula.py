# A = P(1 + r/n)^(nt)


# A = Future amount
# P = Present amount
# R = Percentage (0.06)
# N = # of compounds a year
# T = time 

current = float(input("How much money do you have now? ")) # P
interest = float(input("How much is the interest? (Input in decimal form [6% = 0.06]) ")) # R
compound = float(input("How many times is the interest compounded? ")) # N
time = float(input("How many years? ")) # T

total = current(1 + (interest/compound))**(compound*time)
total += current

print("Your total owed amount after " + str(time) + " years is " + str(total))