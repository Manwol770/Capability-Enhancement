import sys
input = sys.stdin.readline

N, M, start = map(int, input().split())
matrix = [[0]*N for _ in range (N)]
visited_stack = [0]*N
visited_que = [0]*N
stack = [start-1]
que = [start-1]


for _ in range (M) :
    v1, v2 = map(int, input().split())
    matrix[v1-1][v2-1] = 1
    matrix[v2-1][v1-1] = 1

while stack :

    start = stack.pop()

    if visited_stack[start] :
        continue
    else :
        visited_stack[start] = 1
    
    print(start + 1, end = ' ')

    for i in range (N-1,-1,-1) :
        if matrix[start][i] :
            stack.append(i)

print()

while que :

    start = que.pop(0)

    if visited_que[start] :
        continue
    else :
        visited_que[start] = 1

    print(start + 1, end = ' ')

    for i in range (N) :
        if matrix[start][i] :
            que.append(i)