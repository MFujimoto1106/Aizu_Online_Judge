from collections import deque, defaultdict

D = defaultdict(lambda: deque())
color = [None] * 100000


def dfs(node, friend):
    S = deque()
    S.append(node)
    color[node] = friend
    while S:
        u = S.popleft()
        for v in D[u]:
            if color[v] is None:
                color[v] = friend
                S.append(v)


n, m = map(int, input().split())

for _ in range(m):
    s, t = map(int, input().split())
    D[s].append(t)
    D[t].append(s)

friend = 1
for node in range(n):
    if color[node] is None:
        dfs(node, friend)
        friend += 1

q = int(input())

for _ in range(q):
    s, t = map(int, input().split())
    if color[s] == color[t]:
        print('yes')
    else:
        print('no')
