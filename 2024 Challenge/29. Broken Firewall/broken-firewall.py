from os import path

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

shipwifi = 0
passwifi = 0

for x in content:
    inc = int(x[4:8], 16)
    if int(x[24:26], 16) == 192 and int(x[26:28], 16) == 168 and 0 <= int(x[28:30], 16) <= 254 and 0 <= int(x[30:32], 16) <= 254:
        shipwifi += inc
    else:
        passwifi += inc
print(f"{shipwifi}/{passwifi}")
