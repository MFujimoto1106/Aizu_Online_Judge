import sys
sys.setrecursionlimit(2**16 - 1)


def dfs(current, prev):
    global timer
    prenum[current] = lowest[current] = timer
    parent[current] = prev
    timer += 1
    visited[current] = True

    for nxt in Q[current]:
        if not visited[nxt]:
            parent[nxt] = current
            dfs(nxt, current)
            lowest[current] = min(lowest[current], lowest[nxt])
        elif nxt != prev:
            lowest[current] = min(lowest[current], prenum[nxt])


def art_points(root):
    out = set()
    np = root
    for u, p in enumerate(parent):
        if p is None:
            continue
        elif p == root:
            np += 1

        if prenum[p] <= lowest[u]:
            out.add(p)
    if np == 1:
        out.remove(0)
    return out


V, E = map(int, input().split())
Q = [[] for _ in range(V)]
for _ in range(E):
    s, t = map(int, input().split())
    Q[s].append(t)
    Q[t].append(s)

prenum = [None] * V
parent = [None] * V
lowest = [None] * V
timer = 0
visited = [False] * V

dfs(0, None)
out = list(art_points(0))
out.sort()
if out:
    print(*out, sep='\n')
else:
    pass
