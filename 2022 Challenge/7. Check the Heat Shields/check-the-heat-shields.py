import os
from math import prod

filename = "check-the-heat-shields.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [[int(y) for y in x.split()] for x in f.read().splitlines()]

hcf_list = []
for i in content:
    hcf_list.append(i[:])
def func_hcf(lst):
    hcf = lst[0]
    for i in range(1, len(lst)):
        while lst[i]:
            hcf, lst[i] = lst[i], hcf % lst[i]
    return hcf
hcf = func_hcf([func_hcf(i) for i in hcf_list])

for i in range(0, len(content)):
    for j in range(0, len(content[i])):
        content[i][j] //= hcf

final = set()
grid = (20000, 100000)
for i in content:
    for j in range(i[0], i[0]+i[2]):
        for k in range(i[1], i[1]+i[3]):
            final.add((j, k))
print(prod(grid)-(len(final)*(hcf**2))) # Answer: 154807700