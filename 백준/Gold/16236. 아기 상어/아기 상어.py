import sys

input = sys.stdin.readline
from collections import deque


def bfs(x, y, cnt, size):
    global exp
    global time
    visited = [[0] * N for _ in range(N)]

    que = deque()
    que.append((x, y))
    visited[x][y] = cnt
    time = max(time, visited[x][y] - 1)
    pass_list = deque()

    while que:

        x, y = que.popleft()

        if cnt != visited[x][y]:
            cnt = visited[x][y]
            if pass_list:
                pass_list = deque(sorted(pass_list, key=lambda l: (l[0], l[1])))
                x, y = pass_list.popleft()
                matrix[x][y] = 0
                exp += 1
                if exp == size :
                    exp = 0
                    size += 1
                return bfs(x,y,cnt,size)

        for k in range(4):

            nx = x + delta[k][0]
            ny = y + delta[k][1]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if matrix[nx][ny] < size and matrix[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    pass_list.append((nx, ny))
                    que.append((nx,ny))
                    # exp += 1
                    # if exp == size :
                    #     exp = 0
                    #     size += 1
                elif matrix[nx][ny] == size or matrix[nx][ny] == 0:
                    que.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
delta = ((-1, 0), (0, -1), (0, 1), (1, 0))
time = 0
exp = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            x = i
            y = j
            matrix[i][j] = 0

bfs(x, y, 1, 2)
print(time)
