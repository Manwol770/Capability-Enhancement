import sys

input = sys.stdin.readline


def dfs(x, y, num, m, T_F):
    global max_num

    if not (x_k == x or y_k == y):
        return

    for i in range(4):

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:

            if matrix[nx][ny] == m and T_F == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, num + 1, m, 0)
                visited[nx][ny] = 0
                if max_num < num:
                    max_num = num


            elif matrix[nx][ny] == m and matrix[x][y] != m and T_F == 1:
                matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
                dfs(x, y, num + 1, m, 1)
                matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
                if max_num < num:
                    max_num = num


            elif matrix[nx][ny] == m and T_F == 1:
                visited[nx][ny] = 1
                dfs(nx, ny, num + 1, m, 1)
                visited[nx][ny] = 0
                if max_num < num:
                    max_num = num


            elif matrix[nx][ny] != m and T_F == 0:
                visited[nx][ny] = 1
                dfs(nx, ny, num, m, 1)
                visited[nx][ny] = 0
                if max_num < num:
                    max_num = num
    else:
        if max_num < num:
            max_num = num
        return

N = int(input())
max_num = 0
matrix = [list(input().strip()) for _ in range(N)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        visited[i][j] = 1
        x_k, y_k = i, j
        dfs(i, j, 1, matrix[i][j], 0)
        visited[i][j] = 0
print(max_num)