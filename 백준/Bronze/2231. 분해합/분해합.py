import sys
input = sys.stdin.readline

ipt_num = int(input())

for i in range (1, ipt_num+1) :
    sum_line_num = sum((map(int, str(i))))
    sum_num = i + sum_line_num
    if sum_num == ipt_num :
        print(i)
        break
    if i == ipt_num :
        print(0)