import sys
input = sys.stdin.readline

from collections import deque

visited = [-1] * 100001
cnt = 0

N, M = map(int, input().split())

q = deque([])
q.append(N)
visited[N] = 0

while q:

    x = q.popleft()

    if x == M:
        cnt += 1

    for i in range (3):
        if i == 0:
            nx = x + 1
        elif i == 1:
            nx = x - 1
        else :
            nx = x * 2

        if 0 <= nx < 100001:
            if visited[nx] == -1 or visited[nx] > visited[x]:
                q.append(nx)
                visited[nx] = visited[x] + 1
print(visited[M])
print(cnt)