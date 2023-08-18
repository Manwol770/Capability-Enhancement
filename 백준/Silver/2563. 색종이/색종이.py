import sys
input = sys.stdin.readline

N = int(input())
N_list = []
max_x = 0
max_y = 0
for i in range (N) :
    x, y = map(int, input().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    N_list.append((x,y))

graph = [[0]*(max_y+10) for _ in range (max_x+10)]
result = 0

for start, end in N_list :
    for i in range (0,10) :
        for j in range (0,10) :
            if graph[start + i][end + j] == 0 :
                graph[start + i][end + j] = 1
                result += 1
print(result)