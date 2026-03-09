import sys
input = sys.stdin.readline

S = int(input()) - 1
input_str = input().strip()
num_A = 0
num_N = 0
print_num = 0

for i in input_str:
    if i == "A":
        num_A += 1
        if num_A == 2:
            if num_N == 1:
                print_num += 1
            num_A = 1
            num_N = 0
    elif i == "N":
        if num_A == 1:
            num_N += 1
    else:
        continue

print(print_num)