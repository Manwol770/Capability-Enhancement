import sys
input = sys.stdin.readline


N = int(input())
N_list = []
max_num = 0
cnt = 1
for i in range (N) :
    x, y = map(int, input().split())
    N_list.append([x , y])

N_list.sort(key = lambda x : (x[1],x[0]))

e_time = N_list[0][1]
for i in range (1,N) :
    if N_list[i][0] >= e_time :
        e_time = N_list[i][1]
        cnt += 1

print(cnt)