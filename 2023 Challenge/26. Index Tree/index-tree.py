import os

filename = "index-tree.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = [int(x, 16) for x in f.read().splitlines()]

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def traversal(root, depth, levels):
    if root is not None:
        traversal(root.left, depth+1, levels)
        traversal(root.right, depth+1, levels)
        levels[depth] = levels.get(depth, 0)+1
    return levels

def insert(node, val):
    if node is None:
        return Node(val)
    if val < node.val:
        node.left = insert(node.left, val)
    elif val > node.val:
        node.right = insert(node.right, val)
    return node

root = None
for x in content:
    root = insert(root, x)

levels = traversal(root, 0, {})
print(len(levels)*max(levels.values())) # Answer: 30784