import os

filename = "decoding-pixels.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

def output(grid):
    for i in grid:
        for j in i:
            if j:
                print("█", end="")
            else:
                print(" ", end="")
        print()

gridsize = (50, 10)
grid = [[False for _ in range(gridsize[0])] for _ in range(gridsize[1])]

for i in content:
    for j in range(i[0], i[0]+i[2]):
        for k in range(i[1], i[1]+i[3]):
            grid[k][j] = not grid[k][j]
output(grid) # Answer: ncc1701