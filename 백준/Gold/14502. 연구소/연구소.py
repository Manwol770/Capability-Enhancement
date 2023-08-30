import sys

input = sys.stdin.readline

import copy


def dfs(x, y, visited, arr_copy):

    for k in range(4):

        nx = x + delta[k][0]
        ny = y + delta[k][1]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not arr_copy[nx][ny]:
            arr_copy[nx][ny] = 2
            visited[nx][ny] = 1
            dfs(nx, ny, visited, arr_copy)
    return


def wall(x, y, cnt):
    global max_area

    if cnt == 3:
        visited = [[0]*M for _ in range(N)]
        arr_copy = copy.deepcopy(arr)
        free_area = 0
        for v, w in start_point:
            visited[v][w] = 1
            dfs(v, w, visited, arr_copy)
        for i in range(N):
            for j in range(M):
                if arr_copy[i][j] == 0:
                    free_area += 1
        if max_area < free_area:
            max_area = free_area
        return

    for i in range(x, N):
        for j in range(0, M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(i, y, cnt + 1)
                arr[i][j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
max_area = 0
start_point = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            start_point.append((i, j))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            arr[i][j] = 1
            wall(i, j, 1)
            arr[i][j] = 0

print(max_area)