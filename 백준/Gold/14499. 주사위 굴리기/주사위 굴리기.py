import sys
input = sys.stdin.readline

delta = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = []
for i in range(6):
    dice.append([0, 0])
dice[1][1] = 3
dice[2][1] = 1
dice[3][1] = 2
dice[4][1] = 4
dice[5][1] = 5
# print(dice)
N, M, x, y, k = map(int, input().split())
matrix = []

for i in range(N):
    arr = list(map(int, input().split()))
    matrix.append(arr)

arr = list(map(int, input().split()))

start = 0
dice[start][0] = matrix[x][y]

for i in arr:
    i -= 1

    nx = x + delta[i][0]
    ny = y + delta[i][1]

    if 0 <= nx < N and 0 <= ny < M:
        i += 1
        # print(dice)
        # print(f'#{i}')
        x = nx
        y = ny
        if i == 1:
            for j in range(6):
                if dice[j][1] == 0:
                    dice[j][1] = 2
                elif dice[j][1] == 5:
                    dice[j][1] = i
                elif dice[j][1] == i:
                    dice[j][1] = 0
                    if matrix[x][y]:
                        dice[j][0] = matrix[x][y]
                        matrix[x][y] = 0
                    else:
                        matrix[x][y] = dice[j][0]
                elif dice[j][1] == 2:
                    dice[j][1] = 5
        if i == 2:
            for j in range(6):
                if dice[j][1] == 0:
                    dice[j][1] = 1
                elif dice[j][1] == 5:
                    dice[j][1] = i
                elif dice[j][1] == i:
                    dice[j][1] = 0
                    if matrix[x][y]:
                        dice[j][0] = matrix[x][y]
                        matrix[x][y] = 0
                    else:
                        matrix[x][y] = dice[j][0]
                elif dice[j][1] == 1:
                    dice[j][1] = 5
        if i == 3:
            for j in range(6):
                if dice[j][1] == 0:
                    dice[j][1] = 4
                elif dice[j][1] == 5:
                    dice[j][1] = i
                elif dice[j][1] == i:
                    dice[j][1] = 0
                    if matrix[x][y]:
                        dice[j][0] = matrix[x][y]
                        matrix[x][y] = 0
                    else:
                        matrix[x][y] = dice[j][0]
                elif dice[j][1] == 4:
                    dice[j][1] = 5
        if i == 4:
            for j in range(6):
                if dice[j][1] == 0:
                    dice[j][1] = 3
                elif dice[j][1] == 5:
                    dice[j][1] = i
                elif dice[j][1] == i:
                    dice[j][1] = 0
                    if matrix[x][y]:
                        dice[j][0] = matrix[x][y]
                        matrix[x][y] = 0
                    else:
                        matrix[x][y] = dice[j][0]
                elif dice[j][1] == 3:
                    dice[j][1] = 5
        # print(dice)
        for j in range(6):
            if dice[j][1] == 5:
                print(dice[j][0])