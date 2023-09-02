import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range (N)]
delta = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
visited = [[0]*M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            stack = [(i,j)]
            T_F = 0

            while stack:

                x, y = stack.pop()
                visited[x][y] = 1

                for k in range(8):

                    nx = x + delta[k][0]
                    ny = y + delta[k][1]

                    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] > matrix[x][y]:
                        T_F = 1

                    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == matrix[x][y] and not visited[nx][ny]:
                        stack.append((nx, ny))
            if T_F == 0:
                cnt += 1
print(cnt)