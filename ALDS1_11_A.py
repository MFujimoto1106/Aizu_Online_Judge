n = int(input())
adjMatrix = [[0 for i in range(n)] for j in range(n)]

for i in range(n):
    inp = list(map(int, input().split()))
    vertex = inp[0]
    adjVertex_list = []
    if inp[1] > 0:
        for j in range(inp[1]):
            adjVertex_list.append(inp[2+j])
        for adjVertex in adjVertex_list:
            adjMatrix[vertex-1][adjVertex-1] = 1

for x in adjMatrix:
    print(*x)
    
