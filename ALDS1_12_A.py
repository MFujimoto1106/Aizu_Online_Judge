def prim():
    N = 100
    white = 0
    gray = 1
    black = 2
    color = [white] * N
    d = [float('inf')]*N
    d[0] = 0
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
                if M[u][v] < d[v]:
                    d[v] = M[u][v]
                    p[v] = u
                    color[v] = gray

    out = 0
    for i in range(n):
        if d[i] != float('inf'):
            out += d[i]

    return out


n = int(input())
M = []
for _ in range(n):
    inp = list(map(int, input().split()))
    M.append(inp)

print(prim())
