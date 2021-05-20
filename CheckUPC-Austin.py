#Check if a given UPC code is valid

#----STEPS----
#1. Sum the numbers in the odd positions
#2. Multiply the sum of step 1 by 3
#3. Sum the numbers of the even positions
#4. Add the sums of steps 2 and 3
#5. Subtract the sum of step 4 from the next highest multiple of 10 (example, next highest multiple of 10 for 103 is 110)



def FindUPC(code):
    evens = []
    odds = []
    pos = 0
    for c in code:
        if pos % 2 == 0:
            evens.append(c)
        else:
            odds.append(c)
        pos = pos + 1
    

    #1. Sum the numbers in the odd positions
    sum = 0
    for s in odds:
        sum += int(s)
    result = sum
    sum = 0


    #2. Multiply the sum of step 1 by 3
    result *= 3

    #3. Sum the numbers of the even positions
    for s in evens:
        sum += int(s)
    
    #4. Add the sums of steps 2 and 3
    result += sum
    sum = 0
    
    #5. Subtract the sum of step 4 from the next highest multiple of 10 (example, next highest multiple of 10 for 103 is 110)
    sum = result
    while sum % 10 != 0:
        sum += 1
    
    result = sum - result
    print("The final number should be", result)



    
while True:
    code = input("What is the UPC code? ")
    FindUPC(code)