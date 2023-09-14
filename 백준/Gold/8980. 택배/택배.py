import sys
input = sys.stdin.readline


N, capacity = map(int, input().split())
M = int(input())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    give_num, take_num, weight = map(int, input().split())
    matrix[give_num][take_num] = weight

current_capacity = 0
cnt = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if matrix[i][j]:
            if current_capacity + matrix[i][j] < capacity:
                current_capacity += matrix[i][j]
                if matrix[i][j] > 0:
                    cnt += matrix[i][j]
                matrix[j][i] = -matrix[i][j]
            else:
                matrix[j][i] = current_capacity - capacity
                cnt += capacity - current_capacity
                current_capacity = capacity

print(cnt)