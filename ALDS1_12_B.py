def dijkstra(s):
    N = 100
    white = 0
    gray = 1
    black = 2
    color = [white] * N
    d = [float('inf')] * N
    d[s] = 0
    p = [-1] * N

    while True:
        mincost = float('inf')
        for i in range(n):
            if (color[i] != black) and (d[i] < mincost):
                mincost = d[i]
                u = i

        if mincost == float('inf'):
            break

        color[u] = black

        for v in range(n):
            if (color[v] != black) and (M[u][v] != -1):
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    p[v] = u
                    color[v] = gray

    for i in range(n):
        print(str(i) + ' ' + str(d[i]))


n = int(input())
M = [[float('inf')] * n for _ in range(n)]
for _ in range(n):
    u, k, *cv = input().split()
    u = int(u)
    k = int(k)
    for i in range(k):
        v = int(cv[2*i])
        c = int(cv[2*i+1])
        M[u][v] = c

dijkstra(0)
