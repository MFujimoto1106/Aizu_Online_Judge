n = int(input())
dict = set()

for i in range(n):
    command, base = input().split()
    if command == 'insert':
        dict.add(base)
    else:
        if base in dict:
            print('yes')
        else:
            print('no')
