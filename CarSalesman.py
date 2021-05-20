#Car Salesman Program
#
#User will input car prices and the program
#will add on fees to the price

price = input("What's the price of the vehice? ")
price = int(price)

tax = price * 0.05
license = price * 0.07
prep = 150
destination = 300

print("\nYour vehicle will cost $", str(price + tax + license + prep + destination))

input("\n\nPress enter to exit.")