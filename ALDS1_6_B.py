def Partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r, 1):
        if A[j] <= x:
            i += 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    return i+1

n = int(input())
A = list(map(int, input().split()))

pivot = Partition(A, 0, n-1)
A1 = A[:pivot]
A2 = A[pivot+1:]

print(' '.join(list(map(str, A1)))
      + ' [' + str(A[pivot]) + '] '
      + ' '.join(list(map(str, A2))))
