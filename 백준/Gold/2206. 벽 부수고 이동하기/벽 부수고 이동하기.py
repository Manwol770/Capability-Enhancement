import sys

input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]

q = deque([(0, 0)])
q2 = set()
visited[0][0] = 1

while q:

    x, y = q.popleft()

    for i in range(4):

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < N and 0 <= ny < M:
            if not matrix[nx][ny] and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            elif matrix[nx][ny] and (visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1):
                q2.add((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

q2 = deque(q2)

while q2:

    x, y = q2.popleft()

    for i in range(4):

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < N and 0 <= ny < M and not matrix[nx][ny]:
            if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                q2.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[N-1][M-1])