from os import path

mode = 1 # 0 = test, 1 = input

filename = "input.txt" if mode else "test.txt"
here = path.dirname(path.abspath(__file__))
filepath = path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split() for x in f.read().splitlines()]

directory_tree = {}
for x in content:
    if x[0] == "Folder:":
        current_folder = int(x[1])
        directory_tree[current_folder] = {}
    elif x[-2] == "[FOLDER":
        directory_tree[current_folder][x[1]] = ("DIR", int(x[-1][:-1]))
    else:
        directory_tree[current_folder][x[1]] = ("FILE", int(x[-1]))

def get_size(directory_tree, folder, delete=False):
    size = 0
    for x in directory_tree[folder]:
        if directory_tree[folder][x][0] == "FILE":
            if delete or "delete" in x or "temporary" in x:
                size += directory_tree[folder][x][1]
            else:
                continue
        if directory_tree[folder][x][0] == "DIR":
            if delete or "delete" in x or "temporary" in x:
                size += get_size(directory_tree, int(directory_tree[folder][x][1]), True)
            else:
                size += get_size(directory_tree, int(directory_tree[folder][x][1]), False)
    return size

print(get_size(directory_tree, 0))
