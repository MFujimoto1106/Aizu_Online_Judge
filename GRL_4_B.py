def topologicalSort():
    WHITE = 0
    GRAY = 1
    color = [WHITE] * V
    out = []

    def bfs(s):
        Q = []
        Q.append(s)
        color[s] = GRAY
        while Q:
            u = Q.pop(0)
            out.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if (indeg[v] == 0) and (color[v] == WHITE):
                    color[v] = GRAY
                    Q.append(v)

    for u in range(V):
        if (indeg[u] == 0) and (color[u] == WHITE):
            bfs(u)

    return out


V, E = map(int, input().split())
graph = [[] for _ in range(V)]
indeg = [0] * V
for _ in range(E):
    s, t = map(int, input().split())
    indeg[t] += 1
    graph[s].append(t)

out = topologicalSort()

for i in range(len(out)):
    print(out[i])
