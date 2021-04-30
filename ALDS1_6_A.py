def CountingSort(A, B, k):
    C = [0] * k
    for i in range(len(A)):
        C[A[i]] += 1
    for j in range(1, k):
        C[j] = C[j] + C[j-1]
    for l in reversed(range(0, len(A))):
        B[C[A[l]] -1] = A[l]
        C[A[l]] -= 1


n = int(input())
A = list(map(int, input().split()))
B = [None] * len(A)
k = max(A) + 1

CountingSort(A, B, k)

print(*B)
