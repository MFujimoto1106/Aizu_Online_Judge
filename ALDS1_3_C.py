from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
output = deque([])


for j in range(n):
    input_command = list(map(str, input().split()))
    if input_command[0] == 'insert':
        output.insert(0, input_command[1])
    elif input_command[0] == 'delete':
        if input_command[1] in output:
            output.remove(input_command[1])
    elif input_command[0] == 'deleteFirst':
        del output[0]
    elif input_command[0] == 'deleteLast':
        del output[-1]


print(' '.join(list(map(str, output))))
