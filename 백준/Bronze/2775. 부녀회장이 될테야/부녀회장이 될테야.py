import sys
input = sys.stdin.readline

T = int(input())

for tc in range (T) :
    k = int(input())
    n = int(input())
    k_n_list = []
    k_n_list.append([x for x in range (1,n+1)])
    
    for i in range (1,k+1) :
        plus_list = []
        for j in range (n) :
            plus_list.append(sum(k_n_list[i-1][:j+1]))
        k_n_list.append(plus_list)
    print(k_n_list[k][n-1])