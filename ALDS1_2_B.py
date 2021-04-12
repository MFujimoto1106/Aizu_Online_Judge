n = int(input())
A = list(map(int, input().split()))

num_swap = 0

for i in range(n):
    min = i
    for j in range(i, n):
        if A[j] < A[min]:
            min = j
    if (min != i):
        temp = A[i]
        A[i] = A[min]
        A[min] =temp
        num_swap += 1

print(' '.join(list(map(str, A))))
print(num_swap)
