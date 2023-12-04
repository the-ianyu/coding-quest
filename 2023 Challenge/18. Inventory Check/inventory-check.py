import os
from math import prod

filename = "inventory-check.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

items = {}
for x in content:
    if x[2] not in items:
        items[x[2]] = 0
    items[x[2]] += int(x[1])
print(prod(items[x]%100 for x in items)) # Answer: 13327755200
