import os

filename = "snakes-on-a-starship.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read().splitlines()

gridsize = (20, 20)
snake = [[0, 0]]
fruitindex = 0
fruits = [[int(y) for y in x.split(",")] for x in content[1].split()]
movedct = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
moves = [movedct[x] for x in content[3]]

score = 0
for move in moves:
    snake.insert(0, [snake[0][0]+move[0], snake[0][1]+move[1]])
    lastmove = snake.pop()
    if snake[0] in snake[1:] or any(x not in range(gridsize[count]) for count, x in enumerate(snake[0])):
        break
    if snake[0] == fruits[fruitindex]:
        score += 100
        fruitindex += 1
        snake.append(lastmove)
    score += 1
print(score) # Answer: 4240