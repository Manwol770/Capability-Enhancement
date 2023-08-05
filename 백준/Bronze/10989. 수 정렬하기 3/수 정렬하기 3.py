import sys
input = sys.stdin.readline

num1 = int(input())
num_dict = {}

for i in range (num1) :
    num2 = int(input())
    
    if num2 in num_dict :
        num_dict[num2] += 1
    else :
        num_dict[num2] = 1

for i in sorted(num_dict) :
    for j in range (num_dict[i]) :
        print(i)