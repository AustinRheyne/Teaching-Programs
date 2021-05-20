import random

unordered = list(range(10))
ordered = []
random.shuffle(unordered)

while len(unordered) > 0:
    lowest = unordered[0]
    for i in unordered:
        if i < lowest:
            lowest = i
    ordered.append(lowest)
    unordered.remove(lowest)

print(ordered)