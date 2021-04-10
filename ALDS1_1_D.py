if __name__ == '__main__':

    n = int(input())
    R = [int(input()) for i in range(n)]

    max_profit = R[1] - R[0]
    min_value = R[0]

    for j in range(1, n):

        if R[j] - min_value > max_profit:
            max_profit = R[j] - min_value

        if R[j] < min_value:
            min_value = R[j]

print(max_profit)
