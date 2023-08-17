graph_list = []
max_x = 0
max_y = 0
for i in range (4) :
    x1, y1, x2, y2 = map(int, input().split())
    max_x = max(x1, x2, max_x)
    max_y = max(y1, y2, max_y)
    graph_list.append((x1, y1, x2, y2))

graph = [[0]*max_y for _ in range (max_x)]

result = 0
for x1,y1,x2,y2 in graph_list :
    for i in range (x1,x2) :
        for j in range (y1,y2) :
            if graph[i][j] == 0 :
                graph[i][j] = 1
                result += 1

print(result)