import os
from hashlib import sha256

filename = "spot-the-forgery.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split("|") for x in f.read().splitlines()]

def hasher(x:str):
    return sha256(x.encode()).hexdigest()

untampered = True
for i in range(0, len(content)):
    if untampered:
        if hasher(f"{content[i][0]}|{content[i][1]}|{content[i][2]}") == content[i][3]:
            continue
        else:
            untampered = False
    content[i][1] = 0
    content[i][2] = content[i-1][3]
    while True:
        if code := hasher(f"{content[i][0]}|{content[i][1]}|{content[i][2]}")[:6] == "000000":
            content[i][3] = code
            break
        content[i][1] += 1
print(content) # Answer: 000000b60719f04f18d3ae69d12449e48d25dbb1d2e0514ff4d8decede19f728