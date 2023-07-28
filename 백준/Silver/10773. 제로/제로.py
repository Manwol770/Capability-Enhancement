import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for i in range (N) :
    
    num = int(input())
    if num != 0 :
        num_list.append(num)
    else :
        num_list.pop()

print(sum(num_list))