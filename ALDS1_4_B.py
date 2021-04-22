def binary_search(S, key):
    left = 0
    right = len(S)
    while left < right:
        mid = int((left + right) / 2)
        if S[mid] == key:
            return mid
        elif key < S[mid]:
            right = mid
        else:
            left = mid + 1
    return "NOT_FOUND"


n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

count = 0
for i in range(q):
    if binary_search(S, T[i]) != "NOT_FOUND":
        count += 1

print(count)
