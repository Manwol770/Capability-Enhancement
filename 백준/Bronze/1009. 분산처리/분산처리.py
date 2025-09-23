import sys
input = sys.stdin.readline

T = int(input())

for i in range (0, T):
    a, b = map(int, input().split())
    a %= 10
    print_num = a
    for i in range(b - 1):
        print_num = (print_num * a) % 10
    if a == 0:
        print(10)
    else:
        print(print_num)