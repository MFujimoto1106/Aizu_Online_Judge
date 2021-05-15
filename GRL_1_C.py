from copy import deepcopy


def warshall_floyd(n, M):
    m = deepcopy(M)
    for k in range(n):
        for i in range(n):
            if m[i][k] == float('inf'):
                continue
            for j in range(n):
                if m[k][j] == float('inf'):
                    continue
                m[i][j] = min(m[i][j], m[i][k] + m[k][j])
    return m


V, E = map(int, input().split())
M = [[float('inf')] * V for i in range(V)]
for i in range(V):
    M[i][i] = 0
for _ in range(E):
    s, t, d = map(int, input().split())
    M[s][t] = d

out = warshall_floyd(V, M)

for i in range(V):
    if out[i][i] < 0:
        print('NEGATIVE CYCLE')
        exit()

for i in range(V):
    for j in range(V):
        if out[i][j] == float('inf'):
            out[i][j] = 'INF'
    print(*out[i])
