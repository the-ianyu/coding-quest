import os
from math import dist, trunc

filename = "tour-the-stars.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

total = 0
for i in range(1, len(content)):
    total += trunc(dist(content[i-1], content[i]))
print(total) # Answer: 64579603
