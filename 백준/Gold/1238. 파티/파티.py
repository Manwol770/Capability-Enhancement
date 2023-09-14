import sys
input = sys.stdin.readline

from collections import deque

N, M, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]
visited_go_min = [0]*(N+1)
visited_come_min = [float('inf')]*(N+1)
visited_come_min[0] = 0
for _ in range(M):
    start, end, time = map(int, input().split())
    arr[start].append((end, time))

for i in range(1, N+1):
    visited_go = [float('inf')] * (N + 1)
    q = deque([])
    q.append(i)
    visited_go[i] = 0

    while q:
        j = q.popleft()

        for k, t in arr[j]:
            if visited_go[k] > visited_go[j] + t:
                visited_go[k] = visited_go[j] + t
                q.append(k)
    visited_go_min[i] = visited_go[X]

q = deque([X])
visited_come_min[X] = 0
while q:

    i = q.popleft()

    for j, t in arr[i]:
        if visited_come_min[j] > visited_come_min[i] + t:
            visited_come_min[j] = visited_come_min[i] + t
            q.append(j)
max_time = -1
for i in range(1, N+1):
    max_time = max(max_time, visited_go_min[i] + visited_come_min[i])
print(max_time)