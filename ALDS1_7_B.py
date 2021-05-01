class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


def depth(tree, depth_dict, node_id, d):
    depth_dict[node_id] = d
    if tree[node_id].left is not None:
        depth(tree, depth_dict, tree[node_id].left, d+1)
    if tree[node_id].right is not None:
        depth(tree, depth_dict, tree[node_id].right, d+1)


def height(tree, height_dict, node_id):
    h_left, h_right = 0, 0
    if tree[node_id].left is not None:
        h_left = height(tree, height_dict, tree[node_id].left) + 1
    if tree[node_id].right is not None:
        h_right = height(tree, height_dict, tree[node_id].right) + 1
    out = max(h_left, h_right)
    height_dict[node_id] = out
    return out


def sibling(tree, node_id):
    parent = tree[node_id].parent
    if parent is None:
        return -1
    out = tree[parent].left if tree[parent].left != node_id else tree[parent].right
    if out is None:
        return -1
    return out


def degree(tree, node_id):
    out = 2
    if tree[node_id].left is None:
        out -= 1
    if tree[node_id].right is None:
        out -= 1
    return out


n = int(input())
tree = {key: Node(None, None, None) for key in range(n)}

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != -1:
        tree[tmp[0]].left = tmp[1]
        tree[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        tree[tmp[0]].right = tmp[2]
        tree[tmp[2]].parent = tmp[0]

for key, value in tree.items():
    if value.parent is None:
        root = key
        break

depth_dict = {}
depth(tree, depth_dict, root, 0)
height_dict = {}
height(tree, height_dict, root)


def print_node(node_id):
    if tree[node_id].parent is None:
        parent = -1
    else:
        parent = tree[node_id].parent

    sib = sibling(tree, node_id)
    deg = degree(tree, node_id)
    node_type = 'internal node' if deg != 0 else 'leaf'
    if parent == -1:
        node_type = 'root'

    print(f'node {node_id}: parent = {parent}, sibling = {sib}, degree = {deg}, depth = {depth_dict[node_id]}, height = {height_dict[node_id]}, {node_type}')


for i in range(n):
    print_node(i)
