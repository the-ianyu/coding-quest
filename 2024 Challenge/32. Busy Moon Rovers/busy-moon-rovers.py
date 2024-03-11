from os import path

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

flag = 0
total = 0
distance_table = {}

for content_index, content_value in enumerate(content):
    if content_value == []:
        flag = 1
    if flag == 0: # parse distance table
        if content_index == 0:
            for j in content_value:
                distance_table[j] = {}
        else:
            origin = content_value[0]
            for tablerow_value, destination in zip(content_value[1:], distance_table.keys()):
                distance_table[origin][destination] = int(tablerow_value)
    elif flag == 1: # calculate rover distances
        waypoints = content_value[3:]
        while "->" in waypoints:
            waypoints.remove("->")
        for x in range(len(waypoints)-1):
            total += distance_table[waypoints[x]][waypoints[x+1]]
print(total)
