import sys
input = sys.stdin.readline

num = int(input())
num_list = []
for i in range (num) :
    num_list.append(tuple(map(int,input().split())))
new_list = sorted(num_list,key = lambda x : (x[0], x[1]))
for i in new_list :
    print(i[0], i[1])