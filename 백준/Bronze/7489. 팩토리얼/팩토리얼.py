import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    num = int(input().strip())
    print_num = 1
    if num == 0:
        print(f'{print_num}')
    else:
        for i in range (2, num + 1):
            print_num = print_num * (i)
            print_num %= 100000
            while print_num % 10 == 0:
                print_num //= 10
        print(f'{print_num % 10}')