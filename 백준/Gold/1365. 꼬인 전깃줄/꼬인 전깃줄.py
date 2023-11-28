import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(n):
    if i == 0:
        res.append(line[0])
    if res[-1] < line[i]:
        res.append(line[i])
    else:
        tmp = bisect_left(res, line[i])
        res[tmp] = line[i]


print(n - len(res))