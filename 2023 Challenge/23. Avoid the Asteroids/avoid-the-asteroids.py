import os
from math import floor

filename = "avoid-the-asteroids.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[float(y) for y in x.split()] for x in f.read().splitlines()]

gridsize, grid = (100, 100), set()
for i in content:
    i = [i[0]+i[2]*3600, i[1]+i[3]*3600, i[2], i[3]]
    for j in range(60):
        grid.add((floor(i[0]), floor(i[1])))
        i[0] += i[2]
        i[1] += i[3]
for i in range(gridsize[0]):
    for j in range(gridsize[1]):
        if (i, j) not in grid:
            print(f"{i}:{j}") # Answer: 5:8
            break
    else:
        continue
    break
