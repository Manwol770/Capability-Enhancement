import sys

input = sys.stdin.readline


def dfs(x, y, cnt):
    global max_cnt

    for i in range(4):

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] not in visited_set:
            visited_set.add(matrix[nx][ny])
            dfs(nx, ny, cnt + 1)
            visited_set.remove(matrix[nx][ny])

    max_cnt = max(max_cnt, cnt)


N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
visited_set = set()
visited_set.add(matrix[0][0])
max_cnt = 0
dfs(0, 0, 1)

print(max_cnt)