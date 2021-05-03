import math


n = int(input())
heap_elements = list(map(int, input().split()))

for i in range(1, n+1):
    key = heap_elements[i-1]
    if i == 1:
        left_key = heap_elements[1]
        right_key = heap_elements[2]
        print(f'node {i}: key = {key}, left key = {left_key}, right key = {right_key}, ')
    else:
        parent_key = heap_elements[math.floor(i / 2) - 1]
        if 2*i <= n-1:
            left_key = heap_elements[2*i-1]
            right_key = heap_elements[2*i]
            print(f'node {i}: key = {key}, parent key = {parent_key}, left key = {left_key}, right key = {right_key}, ')
        elif 2*i == n:
            left_key = heap_elements[2*i-1]
            print(f'node {i}: key = {key}, parent key = {parent_key}, left key = {left_key}, ')
        else:
            print(f'node {i}: key = {key}, parent key = {parent_key}, ')
