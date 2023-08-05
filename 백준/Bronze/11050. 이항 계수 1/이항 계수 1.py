import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = 1
for i in range (1, K+1) :
    num = num*N // i
    N -= 1
print(num)