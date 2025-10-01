import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    ls = list(map(int, input().strip().split()))
    while N != 2:
        if N % 2 == 0:
            for i in range(N//2):
                ls[i] += ls[N-i-1]
            N //= 2
        else:
            for i in range(N//2):
                ls[i] += ls[N-i-1]
            ls[N//2] += ls[N//2]
            N = N // 2 + 1
    if ls[0] > ls[1]:
        print(f'Case #{t + 1}: Alice')
    else:
        print(f'Case #{t + 1}: Bob')