import sys
input = sys.stdin.readline

from collections import deque

T = 0
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while True:
    T += 1
    N = int(input())
    if N == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]

    q = deque([])
    q.append((0, 0))
    visited[0][0] = matrix[0][0]

    while q:

        x, y = q.popleft()

        for k in range(4):

            nx = x + delta[k][0]
            ny = y + delta[k][1]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] > visited[x][y] + matrix[nx][ny]:
                    visited[nx][ny] = visited[x][y] + matrix[nx][ny]
                    q.append((nx, ny))
    print(f'Problem {T}: {visited[N-1][N-1]}')