class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(N)]
        self.rank = [0]*N

    def findSet(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        x = self.findSet(x)
        y = self.findSet(y)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1


n, q = map(int, input().split())
S = UnionFind(n)
for _ in range(q):
    command, x, y = map(int, input().split())
    if command == 0:
        S.unite(x, y)
    else:
        if S.same(x, y):
            print('1')
        else:
            print('0')
