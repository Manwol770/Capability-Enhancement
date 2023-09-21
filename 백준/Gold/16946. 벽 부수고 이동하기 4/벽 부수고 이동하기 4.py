import sys

input = sys.stdin.readline


N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
visited = [[-1] * M for _ in range(N)]
check = [[-1] * M for _ in range(N)]
check_cnt = 0


for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0 and visited[i][j] == -1:
            cnt = 1
            stack = [(i, j)]
            visited[i][j] = 0
            check_cnt += 1

            while stack:

                x, y = stack.pop()

                for k in range(4):

                    nx = x + delta[k][0]
                    ny = y + delta[k][1]

                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and not matrix[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = 0
                        cnt += 1

            stack = [(i, j)]
            check[i][j] = check_cnt

            while stack:

                x, y = stack.pop()

                if visited[x][y] == cnt:
                    continue
                else:
                    visited[x][y] = cnt

                for k in range(4):

                    nx = x + delta[k][0]
                    ny = y + delta[k][1]

                    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and check[nx][ny] != check_cnt:
                        stack.append((nx, ny))
                        check[nx][ny] = check_cnt
                    if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1 and check[nx][ny] != check_cnt:
                        if visited[nx][ny] == -1:
                            visited[nx][ny] = cnt + 1
                            check[nx][ny] = check_cnt
                        else:
                            visited[nx][ny] += cnt
                            check[nx][ny] = check_cnt

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            if visited[i][j] == -1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = visited[i][j] % 10


for i in range(N):
    for j in range(M):
        print(matrix[i][j], end='')
    print()
