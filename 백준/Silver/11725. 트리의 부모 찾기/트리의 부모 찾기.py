import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
Tree = [[] for i in range(N + 1)]
Tree_p = [0]*(N+1)
q = deque([1])
Tree_p[1] = 1
for i in range(N-1):
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

while q:
    current_node = q.popleft()

    for i in Tree[current_node]:
        if not Tree_p[i]:
            Tree_p[i] = current_node
            q.append(i)

for i in range(2,N+1):
    print(Tree_p[i])