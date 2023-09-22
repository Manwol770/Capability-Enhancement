import sys

input = sys.stdin.readline


def find(a):
    if p_list[a] == a:
        return a

    return find(p_list[a])


def union(a, b):
    x = find(a)
    y = find(b)

    p_list[x] = y


def binarysearch(key):
    start = 0
    end = M - 1
    while start <= end:
        middle = (start + end) // 2
        if M_list[middle] <= key:
            start = middle + 1
        elif M_list[middle] > key:
            end = middle - 1
    return start


N, M, K = map(int, input().split())
p_list = [i for i in range(0, M + 1)]
M_list = list(map(int, input().split()))
M_list.sort()
card_game = list(map(int, input().split()))
for i in card_game:
    key = binarysearch(i)
    print(M_list[find(key)])
    union(find(key), find(key) + 1)