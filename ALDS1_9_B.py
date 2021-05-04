def maxheapify(A, i):
    l = 2 * i + 1
    r = 2 * i + 2
    if l <= H-1:
        if A[l] > A[i]:
            largest = l
        else:
            largest = i
    else:
        largest = i
    if r <= H-1:
        if A[r] > A[largest]:
            largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxheapify(A, largest)


def buildMaxHeap(A):
    for i in reversed(range(0, int(len(A) / 2))):
        maxheapify(A, i)
    return A


H = int(input())
A = list(map(int, input().split()))

out = buildMaxHeap(A)
print('', *out)
