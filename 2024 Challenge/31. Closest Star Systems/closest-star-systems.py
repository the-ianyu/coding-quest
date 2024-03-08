from os import path
from math import dist

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

coordinates = {}
for i in content[1:]:
    coordinates[str(i[:-4])] = (float(i[-3]), float(i[-2]), float(i[-1]))

minimum = float("inf")
for i in coordinates:
    for j in coordinates:
        if i != j:
            minimum = min(minimum, dist(coordinates[i], coordinates[j]))
print(round(minimum, 3))
