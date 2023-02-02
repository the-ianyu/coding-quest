import os
from math import prod

filename = "snakes-and-ladders.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

grid_size = (20, 20)
grid, playerlocations = [], [0, 0]
for i in range(grid_size[1]-1, -1, -1):
    if i % 2 ^ grid_size[1] % 2:
        for j in range(0, grid_size[0]):
            grid.append(content[i][j])
    else:
        for j in range(grid_size[0]-1, -1, -1):
            grid.append(content[i][j])
content = content[grid_size[1]:]

def endcheck(x, y):
    if playerlocations[y]+1 >= prod(grid_size):
        print(prod([x+1, y+1])) # Answer: 95
        exit()

for i in range(0, len(content)):
    for j in range(0, 2):
        playerlocations[j] += content[i][j]
        endcheck(i, j)
        while grid[playerlocations[j]]:
            playerlocations[j] += grid[playerlocations[j]]
            endcheck(i, j)