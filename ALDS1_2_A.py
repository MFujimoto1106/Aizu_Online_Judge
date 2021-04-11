n = int(input())
A = list(map(int, input().split()))

num_swap = 0

for i in range(n):
    for j in range(n-1, i, -1):
       if A[j] < A[j-1]:
           tmp = A[j]
           A[j] = A[j-1]
           A[j-1] = tmp
           num_swap += 1

print(' '.join(list(map(str, A))))
print(num_swap)
