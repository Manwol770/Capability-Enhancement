import sys
from collections import deque
import copy

input = sys.stdin.readline


def permutation(i, K):
    global min_matrix

    if i == K:

        arr = copy.deepcopy(matrix)
        for r, c, s in rotate:
            rotation(r, c, s, arr)
        for i in range(N):
            min_matrix = min(sum(arr[i]), min_matrix)
    else:
        for j in range(i, K):
            rotate[i], rotate[j] = rotate[j], rotate[i]
            permutation(i + 1, K)
            rotate[i], rotate[j] = rotate[j], rotate[i]


def rotation(r, c, s, mat):
    x_sum_rs, y_sum_cs = r + s - 1, c + s - 1
    x_min_rs, y_min_cs = r - s - 1, c - s - 1

    visited = [[0] * M for _ in range(N)]

    while x_min_rs < x_sum_rs:
        stack1 = deque([(x_min_rs, y_min_cs + 1)])
        que2 = deque([mat[x_min_rs][y_min_cs]])
        while stack1:

            x, y = stack1.pop()

            if visited[x][y] == 0:
                visited[x][y] = 1
                que2.append(mat[x][y])
                mat[x][y] = que2.popleft()
            else:
                continue

            for k in range(4):

                nx = x + delta[k][0]
                ny = y + delta[k][1]

                if x_min_rs <= nx <= x_sum_rs and y_min_cs <= ny <= y_sum_cs and visited[nx][ny] == 0:
                    if nx == x_min_rs or nx == x_sum_rs or ny == y_min_cs or ny == y_sum_cs:
                        stack1.append((nx, ny))
        x_min_rs += 1
        x_sum_rs -= 1
        y_min_cs += 1
        y_sum_cs -= 1
    return mat


N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]
min_matrix = float('inf')
rotate = []
for l in range(K):
    rotate.append(list(map(int, input().split())))
permutation(0, K)
print(min_matrix)