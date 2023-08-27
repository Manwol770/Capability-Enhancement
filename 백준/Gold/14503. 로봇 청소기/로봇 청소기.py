import sys

input = sys.stdin.readline


def dfs(x, y, k):
    global cnt
    global T_F

    if visited[x][y] == -1:
        visited[x][y] = cnt
        matrix[x][y] = 2
        cnt += 1

    for d in range(3,-1,-1):

        nx = x + delta[(k+d) % 4][0]
        ny = y + delta[(k+d) % 4][1]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and matrix[nx][ny] != 1:
            dfs(nx, ny, (k+d) % 4)
            if T_F == True :
                return
    nx = x + delta[(k+2) % 4][0]
    ny = y + delta[(k+2) % 4][1]
    if matrix[nx][ny] != 1 :
        dfs(nx,ny,k)
    else :
        T_F = True



N, M = map(int, input().split())
x, y, k = map(int, input().split())
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))      # 바라보고있는 방향
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
cnt = 0
T_F = False

dfs(x, y, k)
print(cnt)