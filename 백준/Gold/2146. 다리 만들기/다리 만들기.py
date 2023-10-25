import sys
input = sys.stdin.readline
from collections import deque
import copy

delta = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs (start, count):
    q = deque([])
    q.append(start)

    while q :

        x, y = q.popleft()

        for i in range(4):

            nx = x + delta[i][0]
            ny = y + delta[i][1]

            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] and visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = count

def find_round ():
    for i in range(n):
        for j in range(n):
            x = i
            y = j
            if visited[x][y] != -1:
                for k in range(4):
                    nx = x + delta[k][0]
                    ny = y + delta[k][1]

                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                        que.append((x, y, 0, visited[x][y]))
                        break

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
min_num = float('inf')
in_count = 10001

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and visited[i][j] == -1:
            visited[i][j] = in_count
            bfs((i, j), in_count)
            in_count += 1

que = []
find_round()
q = deque([])
for i in que:
    q.append(i)
    copy_visited = copy.deepcopy(visited)
    while q:
        x, y, count, land_num = q.popleft()
        if count >= min_num:
            continue
        
        for i in range(4):

                nx = x + delta[i][0]
                ny = y + delta[i][1]

                if 0 <= nx < n and 0 <= ny < n and (copy_visited[nx][ny] == -1 or copy_visited[nx][ny] > count + 1):
                    if copy_visited[nx][ny] != land_num and copy_visited[nx][ny] > 10000:
                        min_num = min(min_num, count)
                        break
                    elif copy_visited[nx][ny] <= 10000:
                        q.append((nx, ny, count + 1, land_num))
                        copy_visited[nx][ny] = count + 1
    # print(copy_visited)

print(min_num)