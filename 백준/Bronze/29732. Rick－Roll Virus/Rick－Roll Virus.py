import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
haru_con = list(input().strip())
n_haru_con = ['.' for i in range(N)]

for i in range(N):
    if haru_con[i] == 'R':
        for j in range(max(0, i-K), min(N, i+K+1)):
            n_haru_con[j] = 'R'

no_p = 0

for i in range(N):
    if n_haru_con[i] == 'R':
        no_p += 1

if no_p > M:
    print('No')
else:
    print('Yes')