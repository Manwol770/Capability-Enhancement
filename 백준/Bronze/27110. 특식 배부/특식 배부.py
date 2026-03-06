import sys

input = sys.stdin.readline

N = int(input())

a, b, c = map(int, input().split())
lis = [a, b, c]
answer = 0

for i in lis:
    answer += min(N, i)

print(answer)