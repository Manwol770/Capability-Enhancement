import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
matrix = [[-1] * N for _ in range(N)]
visited = [float('inf')] * N
link_visited = [0] * N

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
                link_visited[w] = v

print_cnt = 0
print_nodes = []
q = deque([end_point])
while q:
    current_node = q.popleft()
    print_cnt += 1
    print_nodes.append(current_node + 1)
    if current_node == start_point:
        break
    q.append(link_visited[current_node])

print_nodes.reverse()
print(visited[end_point])
print(print_cnt)
for i in range (print_cnt):
    print(print_nodes[i], end = ' ')