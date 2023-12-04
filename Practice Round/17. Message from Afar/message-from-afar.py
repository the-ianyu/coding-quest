import os

filename1, filename2 = "message-from-afar.txt", "character-table.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath1, filepath2 = os.path.join(here, filename1), os.path.join(here, filename2)

with open(filepath1, "r") as f:
    content = bin(int(f.read(), 16))[2:]

with open(filepath2, "r") as f:
    character_table = [x.split() for x in f.read().splitlines()]

current, finalstr = "", ""
while content != "":
    current += content[0]
    content = content[1:]
    for x in character_table:
        if x[1] == current:
            finalstr += x[0]
            current = ""
            break
print(finalstr) # Answer: 1764
