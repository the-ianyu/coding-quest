from os import path

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

tunnels = []
tunnel = []
for x in content:
    if x != "":
        tunnel.append([0 if x == "#" else 1 if x == "." else 2 if x == "$" else None for x in x])
    else:
        tunnels.append(tunnel)
        tunnel = []
tunnels.append(tunnel)

differences = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
]

def bfs_3d(grid, start, end):
    global differences
    visited = set()
    queue = [(start, [start])]
    while queue:
        (x, y, z), path = queue.pop(0)
        if (x, y, z) not in visited:
            visited.add((x, y, z))
            if (x, y, z) == end:
                return path
            for dx, dy, dz in differences:
                nx, ny, nz = x + dx, y + dy, z + dz
                if 0 <= nx < abscissa and 0 <= ny < ordinate and 0 <= nz < applicate and grid[nz][ny][nx] != 0 and (nx, ny, nz) not in visited:
                    if dz != 0 and (grid[z][ny][nx] != 2 or grid[nz][ny][nx] != 2):
                        continue
                    queue.append(((nx, ny, nz), path + [(nx, ny, nz)]))
    return None

abscissa, ordinate, applicate = len(tunnels[0][0]), len(tunnels[0]), len(tunnels)
start = (0, 1, 0)
end = (abscissa-1, ordinate-2, 0)
path = bfs_3d(tunnels, start, end)
length = len(path)
for x in range(len(path)-1):
    if path[x][2] != path[x+1][2]:
        length -= 1
print(length-1)
