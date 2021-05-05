def fibonacci(n):
    if (n == 0) or (n == 1):
        fib_list[n] = 1
        return fib_list[n]
    else:
        if fib_list[n] is not None:
            return fib_list[n]
        fib_list[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_list[n]

      
n = int(input())
fib_list = [None] * 50
print(fibonacci(n))
