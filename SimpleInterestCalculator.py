# I = Prt
# P = Present Amount
# R = Interest rate (5%)
# T = Time in years

current = int(input("How much money do you have now? "))
interest = float(input("How much is the interest? (Input in decimal form [6% = 0.06]) "))
time = int(input("How many years? "))

total = (current * interest * time) + current

print("Total owed amount after " + str(time) + " years will be " + str(total))