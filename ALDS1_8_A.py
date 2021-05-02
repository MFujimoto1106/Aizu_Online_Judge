class Node:
    def __init__(self, parent = None, left = None, right = None):
        self.parent = parent
        self.left = left
        self.right = right


def insert(T, root, z):
    if root == z:
        T[z] = Node()
    else:
        T[z] = Node()
        x = root
        while x is not None:
            next_parent = x
            if z < x:
                x = T[x].left
            else:
                x = T[x].right
        T[z].parent = next_parent

        if z < next_parent:
            T[next_parent].left = z
        else:
            T[next_parent].right = z


def inParse(T, u, inOrder):
    if u is None:
        return
    inParse(T, T[u].left, inOrder)
    inOrder.append(u)
    inParse(T, T[u].right, inOrder)


def preParse(T, u, preOrder):
    if u is None:
        return
    preOrder.append(u)
    preParse(T, T[u].left, preOrder)
    preParse(T, T[u].right, preOrder)


n = int(input())
T = {}

for i in range(n):
    command = list(input().split())
    if command[0] == 'insert':
        z = int(command[1])
        if i == 0:
            root = z
        insert(T, root, z)
    else:
        preOrder, inOrder = [], []
        inParse(T, root, inOrder)
        preParse(T, root, preOrder)
        print("", *inOrder)
        print("", *preOrder)
