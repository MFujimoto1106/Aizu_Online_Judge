class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right


def preParse(u):
    if u is None:
        return
    preOrder.append(u)
    preParse(T[u].left)
    preParse(T[u].right)


def inParse(u):
    if u is None:
        return
    inParse(T[u].left)
    inOrder.append(u)
    inParse(T[u].right)


def postParse(u):
    if u is None:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    postOrder.append(u)


n = int(input())
T = {key: Node(None, None, None) for key in range(n)}

for _ in range(n):
    tmp = list(map(int, input().split()))
    if tmp[1] != -1:
        T[tmp[0]].left = tmp[1]
        T[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        T[tmp[0]].right = tmp[2]
        T[tmp[2]].parent = tmp[0]

for key, value in T.items():
    if value.parent is None:
        root = key
        break


preOrder, inOrder, postOrder = [], [], []
preParse(root)
inParse(root)
postParse(root)

print('Preorder')
print("", *preOrder)
print('Inorder')
print("", *inOrder)
print('Postorder')
print("", *postOrder)
