import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
matrix = [[0] * N for _ in range(N)]
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

apple_cnt = int(input())
for _ in range(apple_cnt):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1

change_dr_cnt = int(input())
change_dr_list = deque([])
for _ in range(change_dr_cnt):
    a, b = map(str, input().split())
    a = int(a)
    change_dr_list.append((a, b))

dr = 0
stack = [(0, 0)]
time = 0
ch_time, ch_dr = change_dr_list.popleft()
line = deque([(0, 0)])
while stack:

    x, y = stack.pop()
    if time == ch_time:
        if ch_dr == 'D':
            dr = (dr + 1) % 4
        else:
            dr = (dr + 3) % 4
        if change_dr_list:
            ch_time, ch_dr = change_dr_list.popleft()

    nx = x + delta[dr][0]
    ny = y + delta[dr][1]
    time += 1
    if 0 <= nx < N and 0 <= ny < N:
        if (nx, ny) in line:
            break
        if matrix[nx][ny] == 1:
            line.append((nx, ny))
            matrix[nx][ny] = 0
        else:
            line.append((nx, ny))
            line.popleft()
        stack.append((nx, ny))
    else:
        break

print(time)