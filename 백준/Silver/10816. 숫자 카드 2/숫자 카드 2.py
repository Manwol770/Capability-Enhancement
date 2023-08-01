import sys
input = sys.stdin.readline

N = int(input())

num_dict = {}
for i in input().split() :
    if i in num_dict :
        num_dict[i] += 1
    else :
        num_dict[i] = 1

M = int(input())

for j in input().split() :
    if j in num_dict :
        print(f'{num_dict[j]}', end=' ')
    else :
        print(0, end=' ')