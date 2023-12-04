import os

filename = "lost-in-an-alien-market.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[0 if x == "#" else 1 for x in y] for y in [list(x) for x in f.read().splitlines()]]

def getNeighbors(x, y, c):
    global horlen, verlen
    neighbors = []
    if x+1 < verlen:
        if content[x+1][y] == 1:
            neighbors.append((x+1, y, c))
    if y+1 < horlen:
        if content[x][y+1] == 1:
            neighbors.append((x, y+1, c))
    if x >= 0:
        if content[x-1][y] == 1:
            neighbors.append((x-1, y, c))
    if y >= 0:
        if content[x][y-1] == 1:
            neighbors.append((x, y-1, c))
    return neighbors

start, end = (0, content[0].index(1)), ((len(content))-1, content[-1].index(1))
horlen, verlen = len(content[0]), len(content)
marked = [[False for _ in range(horlen)] for _ in range(verlen)]
queue = [(start[0], start[1], 1)]
while len(queue) > 0:
    v = queue.pop()
    if not marked[v[0]][v[1]]:
        marked[v[0]][v[1]] = True
        for w in getNeighbors(*v):
            if not marked[w[0]][w[1]]:
                queue.append((w[0], w[1], w[2]+1))
                if (w[0], w[1]) == end:
                    print(w[2]+1) # Answer: 6723
