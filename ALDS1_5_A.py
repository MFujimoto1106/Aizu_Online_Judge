# Time Limit Exceeded

import sys
input = sys.stdin.readline

def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    return solve(i+1, m) or solve(i+1, m-A[i])


n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))

for m in M:
    if solve(0, m):
        print('yes')
    else:
        print('no')
