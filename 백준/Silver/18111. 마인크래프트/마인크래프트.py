import sys
input = sys.stdin.readline

N,M,B = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range (N)]

max_num = 0
# max_idx = ()
max_cnt = 0
max_time = float('inf')
min_num = float('inf')
# min_idx = ()
min_cnt = 0
min_time = float('inf')

time = 0
for i in range (N) :
    for j in range (M) :
        if max_num < matrix[i][j] :
            max_num = matrix[i][j]
            max_cnt = 0
        if max_num == matrix[i][j] :
            max_cnt += 1
        
        if min_num > matrix[i][j] :
            min_num = matrix[i][j]
            min_cnt = 0
        if min_num == matrix[i][j] :
            min_cnt += 1

while max_num != min_num :

    if B >= min_cnt :
        min_time = min_cnt
    else :
        min_time = float('inf')

    max_time = max_cnt * 2

    if min_time > max_time :
        time += max_time
        B += max_cnt
        max_num -= 1
        for i in range (N) :
            for j in range (M) :
                 if max_num == matrix[i][j] :
                        max_cnt += 1

    elif max_time >= min_time :
        time += min_time
        B -= min_cnt
        min_num += 1
        for i in range (N) :
            for j in range (M) :
                 if min_num == matrix[i][j] :
                    min_cnt += 1
print(time,max_num)