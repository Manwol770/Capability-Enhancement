import sys
input = sys.stdin.readline

N, M = map(int,input().split())
matrix = [list(map(int, input().split())) for _ in range (N)]
delta = [(1,0), (0,1), (0,-1), (-1,0)]
visited = [[-1]*M for _ in range (N)]

for i in range(N) :
    for j in range (M) :

        if matrix[i][j] == 2 :

            start = (i, j)
            visited[i][j] = 0

        elif matrix[i][j] == 0 :
            visited[i][j] = 0

stack = [start]
stack = [start]

while stack :

    x, y = stack.pop(0)

    for i in range (4):

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and matrix[nx][ny] :
            stack.append((nx,ny))
            visited[nx][ny] = visited[x][y] + 1
        elif 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1 and not matrix[nx][ny] :
            visited[nx][ny] = 0


for i in visited :
    for j in i :
        print(j, end = ' ')
    print()