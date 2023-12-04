import os

filename = "wordle-with-friends.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

guesses = """keyless YYBBYYG
society YGYYYBB
phobias BBGBGBG"""
guesses = [x.split() for x in guesses.splitlines()]

b, y_int, y_str, g = [], [], [], {}
for i in guesses:
    for j in range(0, len(i[0])):
        match i[1][j]:
            case "B":
                b.append(i[0][j])
            case "Y":
                y_int.append(j)
                y_str.append(i[0][j])
            case "G":
                g[j] = i[0][j]

for i in range(0, len(content)):
    for j in range(0, len(content[i])):
        if (j in g and content[i][j] != g[j]) or any([content[i][j] == y_str[index] for index, char in enumerate(y_int) if char == j]) or content[i][j] in b:
            break
    else:
        if all(k in content[i] for k in y_str):
            print(content[i]) # Answer: cookies
