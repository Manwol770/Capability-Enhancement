import sys
input = sys.stdin.readline

N, M = map(int,input().split())
N_list = list(map(int, input().split()))

max_num = 0
for i in range (N) :
    for j in range (i+1,N) :
        for k in range (j+1,N) :
            if N_list[i]+N_list[j] +N_list[k] <= M:
                max_num = max(max_num, N_list[i]+N_list[j] +N_list[k])

print(max_num)