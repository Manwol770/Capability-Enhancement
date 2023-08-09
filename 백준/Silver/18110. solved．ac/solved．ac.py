import sys
input = sys.stdin.readline

def my_round (num) :
    return int(num) + [0,1][num - int(num) >= 0.5]

n = int(input())
n_lst = []
if n != 0 :
    for i in range (n) :
        n_lst.append(int(input()))
    n_lst.sort()
    n_cnt = len(n_lst)
    start_point = my_round(n_cnt/100*15)
    end_point = n_cnt - my_round(n_cnt/100*15)

    sum_num = 0
    count = 0
    for i in range (start_point, end_point) :
        sum_num += n_lst[i]
        count += 1

    result = my_round(sum_num/count)
    print(result)
else :
    print(0)