from os import path

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

vals = {}
positive = ["Seat", "Meals", "Luggage", "Fee", "Tax"]
negative = ["Discount", "Rebate"]

for x in content:
    if x[0] not in vals:
        vals[x[0]] = 0
    if x[1] in positive:
        vals[x[0]] += int(x[2])
    elif x[1] in negative:
        vals[x[0]] -= int(x[2])
print(min(vals.values()))
