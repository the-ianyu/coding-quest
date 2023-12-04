import os

filename = "mayday.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [(x[16:], x[14:16], x[12:14], x[:4]) for x in f.read().splitlines()]

valid = []
for i in content:
    if i[3] != "5555" or not sum(int(i[0][x:x+2], 16) for x in range(0, len(i[0]), 2)) % 256 == int(i[1], 16):
        continue
    valid.append(i)
print(bytes.fromhex("".join(x[0] for x in sorted(valid, key=lambda x: x[2]))).decode())
# Answer: This is the SY Titanic II. We have struck an asteroid. Engines non responsive. Please help. Coordinates 242.03 by 182.24 by 92.58. Message ends.
