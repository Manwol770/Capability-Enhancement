import sys
input = sys.stdin.readline

def dfs(i,j):

    stack = [(i,j)]

    while stack:

        x,y = stack.pop()

        for k in range (4):

            nx = x + delta[k][0]
            ny = y + delta[k][1]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] == '#' :
                visited[nx][ny] = 1
                stack.append((nx,ny))
        

T = int(input().rstrip())
for tc in range (1,T+1):
    N, M = map(int, input().split())
    matrix = [list(input().rstrip()) for _ in range (N)]
    visited = [[0]*M for _ in range (N)]
    delta = ((0,1), (0,-1), (1,0), (-1,0))
    cnt = 0
    for i in range (N):
        for j in range (M):
            if matrix[i][j] == '#' and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                dfs(i,j)
    print(cnt)