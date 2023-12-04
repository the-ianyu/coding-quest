import os

filename = "the-route-home.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [x.split(" => ") for x in f.read().splitlines()]

START = "TYC"
END = "EAR"
STOPTIME = 600

visited = {}
unvisited = {x[0]: float("inf") for x in content}
distances = {x[0]: {y.split(":")[0]: int(y.split(":")[1])+STOPTIME for y in x[1].split()} for x in content}
unvisited[START] = 0

def dijkstra(unvisited, visited, currentNode, currentDistance, distances):
    while True:
        for neighbour, distance in distances[currentNode].items():
            if neighbour not in unvisited: 
                continue
            newDistance = currentDistance + distance
            unvisited[neighbour] = min(newDistance, unvisited[neighbour])
        visited[currentNode] = currentDistance
        unvisited.pop(currentNode)
        if not unvisited: 
            break
        candidates = [node for node in unvisited.items() if node[1]]
        currentNode, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
    return visited

print(dijkstra(unvisited, visited, START, 0, distances)[END]-STOPTIME) # Answer: 165127
