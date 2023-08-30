import sys

input = sys.stdin.readline

N = int(input())
dp_max = [[(0, 0), (0, 1), (0, 2)]]
dp_min = [[(0, 0), (0, 1), (0, 2)]]

for i in range(1, N + 1):
    max_list = []
    min_list = []
    N_list = list(map(int, input().split()))
    for j in range(3):

        if j == 0:
            max_list.append((max(N_list[0] + dp_max[0][0][0], N_list[0] + dp_max[0][1][0]), 0))
            min_list.append((min(N_list[0] + dp_min[0][0][0], N_list[0] + dp_min[0][1][0]), 0))
        elif j == 1:
            max_list.append((max(N_list[1] + dp_max[0][0][0],
                                 N_list[1] + dp_max[0][1][0], N_list[1] + dp_max[0][2][0]), 1))
            min_list.append((min(N_list[1] + dp_min[0][0][0],
                                 N_list[1] + dp_min[0][1][0], N_list[1] + dp_min[0][2][0]), 1))
        elif j == 2:
            max_list.append((max(N_list[2] + dp_max[0][1][0], N_list[2] + dp_max[0][2][0]), 2))
            min_list.append((min(N_list[2] + dp_min[0][1][0], N_list[2] + dp_min[0][2][0]), 2))
    dp_max.pop()
    dp_min.pop()
    dp_max.append(max_list)
    dp_min.append(min_list)

print(max(dp_max[0][0][0], dp_max[0][1][0], dp_max[0][2][0]), end=' ')
print(min(dp_min[0][0][0], dp_min[0][1][0], dp_min[0][2][0]), end='')
