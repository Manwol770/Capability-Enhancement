import sys
input = sys.stdin.readline

row, col = map(int, input().split())

maze = [list(map(str,str(input().rstrip()))) for _ in range (row)]
visit = [[0]*col for _ in range(row)]
matrix = [[0]*col for _ in range(row)]

delta = [(1,0), (0,1), (0,-1), (-1,0)]

stack = []
x, y = 0, 0
matrix[x][y] = 1
stack.append((x,y))
visit[x][y] = 1

while stack :

    x,y = stack.pop(0)

    for i in range (4) :

        nx = x + delta[i][0]
        ny = y + delta[i][1]

        if 0 <= nx < row and 0 <= ny < col and visit[nx][ny] == 0 and maze[nx][ny] == '1' :
            matrix[nx][ny] = matrix[x][y] + 1
            visit[nx][ny] = 1
            stack.append((nx,ny))

print(matrix[row-1][col-1])