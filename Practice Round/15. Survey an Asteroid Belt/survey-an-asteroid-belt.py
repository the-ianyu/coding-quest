import os

filename = "survey-an-asteroid-belt.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

def getNeighbors(x, y):
    global horlen, verlen
    neighbors = []
    if x+1 < verlen:
        if content[x+1][y]:
            neighbors.append((x+1, y))
    if y+1 < horlen:
        if content[x][y+1]:
            neighbors.append((x, y+1))
    if x > 0:
        if content[x-1][y]:
            neighbors.append((x-1, y))
    if y > 0:
        if content[x][y-1]:
            neighbors.append((x, y-1))
    return neighbors

def dfs(v):
    global marked
    marked[v[0]][v[1]] = True
    for w in getNeighbors(*v):
        if not marked[w[0]][w[1]]:
            dfs(w)

horlen, verlen = len(content[0]), len(content)
marked = [[False for _ in range(horlen)] for _ in range(verlen)]
totalmass, asteroids = 0, 0
for i in range(0, horlen):
    for j in range(0, verlen):
        totalmass += content[i][j]
        if content[i][j] and not marked[i][j]:
            dfs((i, j))
            asteroids += 1
print(totalmass//asteroids) # Answer: 33
