import os

filename = "lost-in-transmission.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y, 16) for y in x.split()] for x in f.read().splitlines()]

erroneous = [-1, -1]
for i in range(0, len(content)-1):
    values = content[i]
    if not sum(values[:-1])%256 == values[-1]:
        erroneous[0] = i
        difference = sum(values[:-1])%256-values[-1]
        while difference < 0:
            difference += 256
for i in range(0, len(content[0])-1):
    values = [content[x][i] for x in range(0, len(content))]
    if not sum(values[:-1])%256 == values[-1]:
        erroneous[1] = i
print(content[erroneous[0]][erroneous[1]]*(content[erroneous[0]][erroneous[1]]-difference)) # Answer: 297
