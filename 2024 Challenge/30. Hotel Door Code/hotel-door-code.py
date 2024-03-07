from os import path

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().split()

width = 100 if mode else 10
final = ""

for i in range(len(content)):
    if i % 2:
        final += "#"*int(content[i])
    else:
        final += "."*int(content[i])

for i in range(0, len(final)):
    print(final[i], end="")
    if i % width == width-1:
        print()
