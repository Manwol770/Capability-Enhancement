import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().split())
space = [[list(map(int, input().split())) for _ in range (N)] for _ in range (H)]
delta = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,-1), (0,0,1)]
visited = [[[0]*M for _ in range (N)] for _ in range (H)]
que = deque([])

for k in range (H) :
    for i in range (N) :
        for j in range (M) :
                if space[k][i][j] == 1 :
                    que.append((k,i,j))
                    visited[k][i][j] = 1

max_tomato = 1

while que :

    z, x, y = que.popleft()

    for l in range (6) :

        nx = x + delta[l][0]
        ny = y + delta[l][1]
        nz = z + delta[l][2]

        if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and space[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0 :

            space[nz][nx][ny] = space[z][x][y] + 1
            visited[nz][nx][ny] = 1
            que.append((nz,nx,ny))

            max_tomato = max(space[nz][nx][ny], max_tomato)

for k in range(H):
    for i in range(N):
        for j in range(M):
            if space[k][i][j] == 0:
                max_tomato = 0

print(max_tomato-1)