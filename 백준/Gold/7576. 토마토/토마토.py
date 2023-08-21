import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range (N)]
visited = [[0]*M for _ in range (N)]
delta = [(1,0), (0,1), (-1,0), (0,-1)]
que = deque([])

for i in range (N) :
    for j in range (M) :
        if matrix[i][j] == 1 and visited[i][j] == 0 :
            que.append((i,j))

max_day = 1

while que :

    x, y = que.popleft()

    for k in range (4) :
        nx = x + delta[k][0]
        ny = y + delta[k][1]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0 and visited[nx][ny] == 0 :
            matrix[nx][ny] = matrix[x][y] + 1
            que.append((nx, ny))
            if matrix[nx][ny] > max_day :
                max_day = matrix[nx][ny]

for i in range (N) :
    for j in range (M) :
        if matrix[i][j] == 0 :
            max_day = 0

print(max_day-1)