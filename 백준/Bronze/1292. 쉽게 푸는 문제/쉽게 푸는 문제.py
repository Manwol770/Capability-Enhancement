import sys
input = sys.stdin.readline

a,b = map(int, input().split())
num = 0
num_list = []

while len(num_list) != b :
    num += 1
    for i in range (0,num) :
        num_list.append(num)
        if len(num_list) == b :
            break

print(sum(num_list[a-1:b]))