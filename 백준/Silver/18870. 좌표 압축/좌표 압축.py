import sys
input = sys.stdin.readline

num1 = input()
num_list = list(map(int, input().split()))
num_dict = dict(map(lambda x : (x, 0) , num_list))
count = 0

for i in sorted(num_dict) :
    num_dict[f'{i}'] = count
    count += 1

for i in num_list :
    print(num_dict[f'{i}'])