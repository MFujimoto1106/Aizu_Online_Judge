N = 100
white = 0
gray = 1
black = 2

m = [[0]*N for _ in range(N)]
color = [white]*N
d = [0]*N
f = [0]*N

def dfs_visit(u):
    global time
    color[u] = gray
    time += 1
    d[u] = time
    for v in range(n):
        if m[u][v] == 0:
            continue
        if color[v] == white:
            dfs_visit(v)
    color[u] = black
    time += 1
    f[u] = time


def dfs():
    global time
    time = 0
    for u in range(n):
        if color[u] == white:
            dfs_visit(u)
    for u in range(n):
        print(str(u + 1) + ' '
              + str(d[u]) + ' '
              + str(f[u]))


n = int(input())
for _ in range(n):
    u, k, *v_list = input().split()
    u = int(u) - 1
    for v in v_list:
        v = int(v) - 1
        m[u][v] = 1

dfs()
