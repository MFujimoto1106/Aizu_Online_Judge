def Partition(A, p, r):
    x = A[r][1]
    i = p-1
    for j in range(p, r, 1):
        if A[j][1] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1


def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)


n = int(input())
A = []
for _ in range(n):
    suit, num = input().split()
    A.append([suit, int(num)])

A_stably_sorted = sorted(A, key = lambda x:x[1])
Quicksort(A, 0, n-1)
print('Stable' if A == A_stably_sorted else 'Not stable')
for i in A:
    print(*i)
