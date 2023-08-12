import sys
input = sys.stdin.readline

def dfs (x, y, N) :

    visited = [0]*N
    start = x
    goal = y
    stack = [start]

    while stack :
        start = stack.pop()
        
        for i in range (N) :
            if adj_m[start][i] and visited[i] == 0 :
                stack.append(i)
                visited[i] = 1
                if i == goal :
                    return 1
    
    return 0


N = int(input())
adj_m = [list(map(int, input().split())) for _ in range (N)]
matrix = [[0]*N for _ in range (N)]

for i in range (N) :
    for j in range (N) :
        matrix[i][j] = dfs(i, j, N)

for i in range (N) :
    for j in range (N) :
        print(matrix[i][j], end = ' ')
    print()