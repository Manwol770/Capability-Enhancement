import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

visited = [0] * (N+1)

visited_order = 1

stack = [R]

while stack:
    node = stack.pop()

    if not visited[node]:
        visited[node] = visited_order
        visited_order += 1

        for adj in reversed(graph[node]):
            if not visited[adj]:
                stack.append(adj)

for i in range(1, N+1):
    print(visited[i])