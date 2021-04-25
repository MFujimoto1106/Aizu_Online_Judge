def koch(d, p1, p2):

    if d == n:
        return

    s = (2/3 * p1[0] + 1/3 * p2[0], 2/3 * p1[1] + 1/3 * p2[1])
    t = (1 / 3 * p1[0] + 2 / 3 * p2[0], 1 / 3 * p1[1] + 2 / 3 * p2[1])
    # R = [[np.cos(np.pi / 3), -np.sin(np.pi / 3)], [np.sin(np.pi / 3), np.cos(np.pi / 3)]]
    R = [[1 / 2, -0.86602540378], [0.86602540378, 1 / 2]]
    u = (R[0][0] * (t[0] - s[0]) + R[0][1] * (t[1] - s[1]) + s[0],
         R[1][0] * (t[0] - s[0]) + R[1][1] * (t[1] - s[1]) + s[1])


    koch(d+1, p1, s)
    print(*s)
    koch(d+1, s, u)
    print(*u)
    koch(d+1, u, t)
    print(*t)
    koch(d+1, t, p2)


n = int(input())
p1 = (0, 0)
p2 = (100, 0)
print(*p1)
koch(0, p1, p2)
print(*p2)
