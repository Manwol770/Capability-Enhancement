import sys
from collections import deque

input = sys.stdin.readline


def que_append(x1, x2, y):
    if 1 <= x2 <= 1000000 and not arr[x2]:
        que.append((x2, y))
        arr[x2] = x1


N, M = map(int, input().split())
arr = [''] * 1000001
n = 0
k = 1
start = [1, 1]
while True:
    if 6 * (n + 1) + k > 1020000:
        break
    n += 1
    k += 6 * n
    start.append(k)

for i in range(1,580):
    if start[i] >= N:
        n = i - 1
        break
que = deque([])
que.append((N, n))
arr[N] = N

while que:

    x, n = que.popleft()

    if x == M:
        break

    if n == 0:
        for i in range(2, 8):
            if not arr[i]:
                que.append((i, 1))
                arr[i] = x

    elif x == 2:

        que_append(x, x - 1, n - 1)
        que_append(x, x + 1, n)
        que_append(x, start[n] + n * 6, n)
        que_append(x, x + n * 6, n + 1)
        que_append(x, x + n * 6 + 1, n + 1)
        que_append(x, 10, n + 1)

    elif x == start[n] + n * 6:

        que_append(x, x - 1, n)
        que_append(x, x + 1, n + 1)
        que_append(x, start[n] + 1, n)
        que_append(x, x + (n + 1) * 6, n + 1)
        que_append(x, x + (n + 1) * 6 - 1, n + 1)
        que_append(x, x - n * 6, n - 1)

    elif x == start[n] + 1:

        que_append(x, x - 1, n - 1)
        que_append(x, x + 1, n)
        que_append(x, start[n] + n * 6, n)
        que_append(x, x + n * 6, n + 1)
        que_append(x, x + n * 6 + 1, n + 1)
        que_append(x, x - (n - 1) * 6, n - 1)


    elif (x - (start[n])) % n:

        plus_mog = (x - (start[n])) // n
        plus_x = x + n * 6 + plus_mog
        plus_mod = (x - (start[n])) % n


        que_append(x, x - 1, n)
        que_append(x, x + 1, n)
        que_append(x, plus_x, n + 1)
        que_append(x, plus_x + 1, n + 1)
        que_append(x, start[n - 1] + plus_mod + plus_mog * (n - 1), n - 1)
        que_append(x, start[n - 1] + plus_mod + plus_mog * (n - 1) - 1, n - 1)

    elif not (x - (start[n])) % n:

        plus_mog = (x - (start[n])) // n
        plus_x = x + n * 6 + plus_mog

        que_append(x, x - 1, n)
        que_append(x, x + 1, n)
        que_append(x, plus_x, n + 1)
        que_append(x, plus_x + 1, n + 1)
        que_append(x, plus_x - 1, n + 1)
        que_append(x, start[n - 1] + plus_mog * (n - 1), n - 1)
lst = [M]
cnt = 1
while M != N:
    lst.append(arr[M])
    M = arr[M]
    cnt += 1
for i in range (cnt-1,-1,-1):
    print(lst[i], end=' ')