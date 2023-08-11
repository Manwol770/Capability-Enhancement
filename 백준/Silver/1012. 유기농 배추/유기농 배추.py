import sys
input = sys.stdin.readline

def dfs (x,y) :

    visited[x][y] = 1
    stack = [(x, y)]

    delta = ((0,1), (1,0), (-1,0), (0,-1))

    while stack :

        x,y = stack.pop()

        for n in range (4) :
            nx = x + delta[n][0]
            ny = y + delta[n][1]
            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == 0 and matrix[nx][ny] == 1 :
                stack.append((nx, ny))
                visited[nx][ny] = 1
                

T = int(input())

for i in range (1, T+1) :
    col, row, N = map(int, input().split())
    matrix = [[0]*col for _ in range (row)]
    visited = [[0]*col for _ in range (row)]
    for _ in range (N) :
        y, x = map(int, input().split())
        matrix[x][y] = 1

    cnt = 0
    for i in range (row) :
        for j in range (col) :
            if matrix[i][j] and visited[i][j] == 0 :
                cnt += 1
                dfs(i,j)
            else :
                visited[i][j] = 1
    print(cnt)