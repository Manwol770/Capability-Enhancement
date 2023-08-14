import sys
input = sys.stdin.readline

N = int(input())
line = int(input())
matrix = [[0]*N for _ in range (N)]

for i in range (line) :
    n1, n2 = map(int ,input().split())
    matrix[n1-1][n2-1] = 1
    matrix[n2-1][n1-1] = 1

visited = [0] * N
start = 0
stack = [start]
visited[start] = 1

while stack :
    start = stack.pop()
    for i in range (N) :
        if matrix[start][i] and visited[i] == 0 :
            visited[i] = 1
            stack.append(i)

result = 0
for i in visited :
    result += i

print(result-1)