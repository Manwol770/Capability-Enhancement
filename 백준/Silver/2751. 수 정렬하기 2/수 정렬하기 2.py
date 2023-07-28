import sys
input = sys.stdin.readline

import sys

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num.sort()

for i in num:
    print(i)