import sys

input = sys.stdin.readline


def divide(lst1, lst2):
    pb_f = [[(lst1[0][0] * lst2[0][0] + lst1[0][1] * lst2[1][0]) % 1000000000,
             (lst1[0][0] * lst2[0][1] + lst1[0][1] * lst2[1][1]) % 1000000000],
            [(lst1[1][0] * lst2[0][0] + lst1[1][1] * lst2[1][0]) % 1000000000,
             (lst1[1][0] * lst2[0][1] + lst1[1][1] * lst2[1][1]) % 1000000000]]

    return pb_f


def pibo(num):
    if num == 1:
        return [[1, 1], [1, 0]]

    pb_p = pibo(num // 2)
    pb_f = divide(pb_p, pb_p)

    if num % 2:
        return divide(pb_f, [[1, 1], [1, 0]])
    else:
        return pb_f


N, M = map(int, input().split())

if (pibo(M + 2)[1][0] - 1) - (pibo(N + 1)[1][0] - 1) < 0:
    print((pibo(M + 2)[1][0] - 1) - (pibo(N + 1)[1][0] - 1) + 1000000000)
else:
    print((pibo(M + 2)[1][0] - 1) - (pibo(N + 1)[1][0] - 1))