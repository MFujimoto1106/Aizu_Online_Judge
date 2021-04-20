n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for j in range(q):
    if T[j] in S:
        count += 1

print(count)
