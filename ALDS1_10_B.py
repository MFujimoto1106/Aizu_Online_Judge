n = int(input())
p = list(map(int, input().split()))
for _ in range(n-1):
    p.append(int(input().split()[1]))


def matrixChainMultiplication():
    m = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        m[i][i] = 0
    
    for l in range(1, n):
        for i in range(n):
            j = i+l
            if j >= n:
                continue
            for k in range(i, j):
                m[i][j] = min(m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1], m[i][j])
    return m[0][-1]


print(matrixChainMultiplication())
