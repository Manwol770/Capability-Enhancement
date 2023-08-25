import sys
input = sys.stdin.readline
from collections import deque
import copy

def f(num, M, s):

    if 3 == s:
        arr_archer.add(tuple(N_bit))
    elif num == M:
        return

    else :
        N_bit[num] = 1
        f(num+1, M, s+1)
        N_bit[num] = 0
        f(num+1, M, s)

N, M, D = map(int, input().split())
field = [list(map(int, input().split())) for _ in range (N)]
delta = ((0, -1), (-1, 0), (0, 1))
N_bit = [0]*M
arr_archer = set()
f(0, M, 0)

kill_max_sum = 0

for lst in arr_archer :

    kill_sum = 0
    field_copy = copy.deepcopy(field)
    N_copy = N

    for i in range (N_copy) :

        field_copy.append(list(lst))
        kill_archer = []
        for j in range (M):
            if field_copy[N_copy][j] == 1:

                que = deque([(N_copy, j)])
                visited = [[0] * M for _ in range(N_copy + 1)]

                while que:

                    x, y = que.popleft()

                    if x != N_copy and field_copy[x][y] == 1:
                        if (x, y) not in kill_archer:
                            kill_archer.append((x, y))
                        break
                        
                    if visited[x][y] == D:
                        continue

                    for k in range (3) :

                        nx = x + delta[k][0]
                        ny = y + delta[k][1]

                        if 0 <= nx < N_copy and 0 <= ny < M and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            que.append((nx, ny))

        kill_sum += len(kill_archer)
        for x, y in kill_archer:
            field_copy[x][y] = 0
        field_copy.pop()
        field_copy.pop()
        N_copy -= 1
    kill_max_sum = max(kill_max_sum, kill_sum)

print(kill_max_sum)