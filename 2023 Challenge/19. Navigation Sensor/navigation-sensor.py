import os

filename = "navigation-sensor.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

valid = []
for x in content:
    if not bin(y := int(x)).count("1")%2:
        valid.append(y%32768)
print(round(sum(valid)/len(valid))) # Answer: 297
