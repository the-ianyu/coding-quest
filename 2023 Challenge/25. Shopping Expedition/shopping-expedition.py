import os
from itertools import permutations

filename = "shopping-expedition.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

minpath = float("inf")
for i in permutations(range(1, len(content))):
    currentpath = 0
    i = [0] + list(i) + [0]
    for j in range(1, len(i)):
        currentpath += content[i[j-1]][i[j]]
    if currentpath < minpath:
        minpath = currentpath
print(minpath) # Answer: 7524
