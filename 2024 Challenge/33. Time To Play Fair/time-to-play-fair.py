from os import path
from string import ascii_lowercase

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

"""
NOTE: The input data should look like this:
    *key*
    *text*
"""

key = content[0]
text = content[1]

grid = {}
gridtext = iter((''.join(dict.fromkeys(key)) + ''.join(x if x not in key else '' for x in ascii_lowercase.replace('j', '')))[:25])
for hor in range(5):
    for ver in range(5):
        grid[s := (next(gridtext))] = (hor, ver)
        grid[(hor, ver)] = s

fstr = ""
text = text.replace('j', 'i').split()
for i in range(len(text)):
    if len(text[i]) % 2:
        text[i] += 'x' if text[i][-1] != 'x' else 'z'
    tstr = ""
    for j in range(0, len(text[i]), 2):
        char1, char2 = text[i][j], text[i][j+1]
        if grid[char1][0] == grid[char2][0]:
            tstr += grid[(grid[char1][0], (grid[char1][1] - 1) % 5)]
            tstr += grid[(grid[char2][0], (grid[char2][1] - 1) % 5)]
        elif grid[char1][1] == grid[char2][1]:
            tstr += grid[((grid[char1][0] - 1) % 5, grid[char1][1])]
            tstr += grid[((grid[char2][0] - 1) % 5, grid[char2][1])]
        else:
            tstr += grid[(grid[char1][0], grid[char2][1])]
            tstr += grid[(grid[char2][0], grid[char1][1])]
    fstr += tstr + ' '
print(fstr)
