row, column = map(int, input().split())

visited = [[False]*column for _ in range (row)]

poto = []

delta = [(0,1),(1,0),(0,-1),(-1,0)]

count = 0

size_max = 0

def dfs(i,j) :
    x,y = i,j
    stack = [(x,y)]
    visited[x][y] = True
    size = 1

    while stack:
        x,y = stack.pop()
        for o in range (4) :
            nx = x + delta[o][0]
            ny = y + delta[o][1]

            if 0 <= nx < row and 0 <= ny < column and visited[nx][ny] == False and poto[nx][ny] == '1' :
                stack.append((nx,ny))
                visited[nx][ny] = True
                size += 1
    
    return size

for _ in range (row) :
    poto_file = []
    poto_file = input().split()
    poto.append(poto_file)

for i in range (row) :
    for j in range (column) :
        if poto[i][j] == '1' and visited[i][j] == False :
            count += 1
            size = dfs(i,j)
            if size_max <= size :
                size_max = size

print(count,size_max)