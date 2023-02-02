import os

filename = "lottery-tickets.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

total = 0
winning = [int(x) for x in "12 48 30 95 15 55 97".split()]
for i in range(0, len(content)):
    match sum([x in winning for x in content[i]]):
        case 3: total += 1
        case 4: total += 10
        case 5: total += 100
        case 6: total += 1000
print(total) # Answer: 56