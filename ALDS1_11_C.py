N = 100
m = [[0]*N for _ in range(N)]
white = 0
black = 1
color = [white] * N
d = [0]*N
queue = []


def bfs():
    start_id = 0
    queue.append(start_id)
    while len(queue) != 0:
        u = queue.pop(0)
        for v in range(n):
            if m[u][v] == 0:
                continue
            elif color[v] == white:
                queue.append(v)
                d[v] = d[u] + 1
                color[u] = black
                color[v] = black
    for i in range(1, n):
        if d[i] == 0:
            d[i] = -1


n = int(input())
for _ in range(n):
    u, k, *v_list = input().split()
    u = int(u) - 1
    for v in v_list:
        v = int(v) - 1
        m[u][v] = 1

bfs()
for i in range(n):
    print(str(i+1) + ' ' + str(d[i]))
