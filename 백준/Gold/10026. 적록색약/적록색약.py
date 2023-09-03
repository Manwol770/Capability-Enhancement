import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs1(x, y, s):
    for k in range(4):
        nx = x + delta[k][0]
        ny = y + delta[k][1]

        if 0 <= nx < N and 0 <= ny < N and not visited1[nx][ny] and matrix[nx][ny] == s:
            visited1[nx][ny] = 1
            dfs1(nx, ny, s)


def dfs2(x, y, s):
    for k in range(4):
        nx = x + delta[k][0]
        ny = y + delta[k][1]

        if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny]:
            if (matrix[nx][ny] == 'R' and matrix[x][y] == 'G') or (matrix[nx][ny] == 'G' and matrix[x][y] == 'R') or matrix[nx][ny] == s:
                visited2[nx][ny] = 1
                dfs2(nx, ny, matrix[nx][ny])


N = int(input())
matrix = [list(input().strip()) for _ in range(N)]
cnt1 = 0
cnt2 = 0
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            visited1[i][j] = 1
            dfs1(i, j, matrix[i][j])
            cnt1 += 1
        if not visited2[i][j]:
            visited2[i][j] = 1
            dfs2(i, j, matrix[i][j])
            cnt2 += 1
print(cnt1, cnt2)