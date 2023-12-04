import os
from math import prod

filename = "tic-tac-toe.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

def wincheck(moves):
    wincombinations = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["1", "4", "7"],
        ["2", "5", "8"],
        ["3", "6", "9"],
        ["1", "5", "9"],
        ["3", "5", "7"],
    ]
    return True if any(all(i in moves for i in j) for j in wincombinations) else False
    
wincounter = [0, 0, 0]
for x in content:
    for y in range(len(x)):
        if wincheck(x[0:y+1:2]):
            wincounter[0] += 1
            break
        elif wincheck(x[1:y+1:2]):
            wincounter[1] += 1
            break
    else:
        wincounter[2] += 1
print(prod(wincounter)) # Answer: 20938290
