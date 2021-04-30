class Node:
    def __init__(self):
        self.parent = -1
        self.children = []

def depth(node_id, d = 0):
    tree[node_id].depth = d
    for child in tree[node_id].children:
        depth(child, d+1)

n = int(input())
tree = [Node() for _ in range(n)]

for i in range(n):
    info = list(map(int, input().split()))
    node_id = info[0]
    k = info[1]
    if k > 0:
        children = info[2:]
        tree[node_id].children = children
        tree[node_id].type = 'internal node'
    else:
        tree[node_id].type = 'leaf'

    for child in tree[node_id].children:
        tree[child].parent = node_id

root_id = [i for i,t in enumerate(tree) if t.parent == -1][0]
tree[root_id].type = 'root'
depth(root_id)

for i,t in enumerate(tree):
    print("node {}: parent = {}, depth = {}, {}, {}".format(i, t.parent, t.depth, t.type, t.children))
