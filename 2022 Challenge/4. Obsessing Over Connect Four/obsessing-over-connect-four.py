import os
from math import prod

filename = "obsessing-over-connect-four.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

def movement(grid, column, player):
    row = 1
    while True:
        if row <= 6 and grid[row][column-1] == None:
            row += 1
        else:
            grid[row-1][column-1] = player
            return grid

def getwins(grid, wincounts):
    for i in range(0, len(grid)):
        for j in range(3, len(grid)):
            current = [grid[i][x] for x in range(j-3, j+1)]
            if all(x == current[0] for x in current) and None not in current:
                wincounts[current[0]-1] += 1
                return True, wincounts
    for i in range(3, len(grid)):
        for j in range(0, len(grid)):
            current = [grid[x][j] for x in range(i-3, i+1)]
            if all(x == current[0] for x in current) and None not in current:
                wincounts[current[0]-1] += 1
                return True, wincounts
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if i+4 <= len(grid) and j+4 <= len(grid):
                current = [grid[i+x][j+x] for x in range(0, 4)]
                if all(x == current[0] for x in current) and None not in current:
                    wincounts[current[0]-1] += 1
                    return True, wincounts
            if i >= len(grid)-4 and j+4 <= len(grid):
                current = [grid[i-x][j+x] for x in range(0, 4)]
                if all(x == current[0] for x in current) and None not in current:
                    wincounts[current[0]-1] += 1
                    return True, wincounts
    return False, wincounts

wincounts = [0, 0, 0]
for i in content:
    grid = [[None for _ in range(7)] for _ in range(7)]
    for j in range(0, len(i)):
        grid = movement(grid, int(i[j]), j%3+1)
        terminator, wincounts = getwins(grid, wincounts)
        if terminator:
            break
print(prod(wincounts)) # Answer: 21630678