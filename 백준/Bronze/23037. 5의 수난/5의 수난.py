import sys

input = sys.stdin.readline

input_num = input().strip()
split_num = list(map(int, list(input_num)))
print_num = 0

for i in split_num:
    print_num += i**5

print(print_num)