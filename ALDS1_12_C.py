from heapq import heapify, heappop, heappush, heappushpop


class priorityQueue:
    def __init__(self, heap):
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)


def dijkstra(s):
    N = 10000
    white = 0
    gray = 1
    black = 2
    color = [white] * N
    d = [float('inf')] * N
    d[s] = 0
    p = [None] * N
    PQ = priorityQueue([(0, s)])

    while PQ:
        mincost, u = PQ.pop()

        color[u] = black

        if d[u] < mincost:
            continue

        for adj_u in adj[u]:
            v = adj_u[0]
            if color[v] == black:
                continue
            if d[v] > d[u] + adj_u[1]:
                d[v] = d[u] + adj_u[1]
                p[v] = u
                PQ.push((d[v], v))
                color[v] = gray

    for i in range(n):
        print(i, d[i])


n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n):
    u, k, *vc = map(int, input().split())
    if k != 0:
        for i in range(k):
            adj[u].append((vc[2*i], vc[2*i+1]))

dijkstra(0)
