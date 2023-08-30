import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
matrix = [[-1] * N for _ in range(N)]
visited = [float('inf')] * N

for _ in range(M):
    start, end, pay = map(int, input().split())
    start -= 1
    end -= 1
    if matrix[start][end] == -1 or matrix[start][end] > pay:
        matrix[start][end] = pay

start_point, end_point = map(int, input().split())
start_point -= 1
end_point -= 1
q = deque([])
q.append(start_point)
visited[start_point] = 0

while q:

    v = q.popleft()

    for w in range(N):
        if matrix[v][w] != -1:
            if visited[v] + matrix[v][w] < visited[w]:
                visited[w] = visited[v] + matrix[v][w]
                q.append(w)

print(visited[end_point])