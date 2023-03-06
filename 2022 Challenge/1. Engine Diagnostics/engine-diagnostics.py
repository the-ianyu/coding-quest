import os

filename = "engine-diagnostics.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [int(x) for x in f.read().splitlines()]

total = 0
for i in range(60, len(content)):
    r_av = sum(content[i-60:i])/60
    total += 1 if r_av < 1500 or r_av > 1600 else 0
print(total) # Answer: 6248