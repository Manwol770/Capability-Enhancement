import sys

input = sys.stdin.readline

import heapq

N, Q = map(int, input().split())
p = [[] for i in range(N)]
cnt = 0


for i in range(Q):
    cnt += 1
    s, e, painting = map(int, input().split())
    s -= 1
    e -= 1
    p[s].append((cnt, e, painting))

heap = []
heapq.heappush(heap, (100001, 100001, 0))

for i in range(N):
    if p[i]:
        for j in range(len(p[i])):
            heapq.heappush(heap, p[i][j])
    
    print(heap[0][2], end=' ')

    while heap[0][1] <= i:
        heapq.heappop(heap)