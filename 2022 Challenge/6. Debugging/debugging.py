import os

filename = "debugging.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

line = 0
variables = {letter: 0 for letter in "ABCDEFGHIJKL"}
while line < len(content):
    command = content[line].split()
    line += 1
    match command[0]:
        case "ADD":
            if command[2].strip("-").isnumeric():
                variables[command[1]] += int(command[2])
            else:
                variables[command[1]] += variables[command[2]]
        case "MOD":
            if command[2].strip("-").isnumeric():
                variables[command[1]] %= int(command[2])
            else:
                variables[command[1]] %= variables[command[2]]
        case "DIV":
            if command[2].strip("-").isnumeric():
                variables[command[1]] //= int(command[2])
            else:
                variables[command[1]] //= variables[command[2]]
        case "MOV":
            if command[2].strip("-").isnumeric():
                variables[command[1]] = int(command[2])
            else:
                variables[command[1]] = variables[command[2]]
        case "JMP":
            if command[1].strip("-").isnumeric():
                line += int(command[1])-1
            else:
                line += variables[command[1]]-1
        case "JIF":
            if recent:
                if command[1].strip("-").isnumeric():
                    line += int(command[1])-1
                else:
                    line += variables[command[1]]-1
        case "CEQ":
            if command[1].strip("-").isnumeric() and command[2].strip("-").isnumeric():
                recent = int(command[1]) == int(command[2])
            elif command[1].strip("-").isnumeric():
                recent = int(command[1]) == variables[command[2]]
            elif command[2].strip("-").isnumeric():
                recent = variables[command[1]] == int(command[2])
            else:
                recent = variables[command[1]] == variables[command[2]]
        case "CGE":
            if command[1].strip("-").isnumeric() and command[2].strip("-").isnumeric():
                recent = int(command[1]) >= int(command[2])
            elif command[1].strip("-").isnumeric():
                recent = int(command[1]) >= variables[command[2]]
            elif command[2].strip("-").isnumeric():
                recent = variables[command[1]] >= int(command[2])
            else:
                recent = variables[command[1]] >= variables[command[2]]
        case "OUT":
            if command[1].strip("-").isnumeric():
                print(command[1], end=" ")
            else:
                print(variables[command[1]], end=" ") # Answer: 7745743850156157
        case "END":
            exit()
