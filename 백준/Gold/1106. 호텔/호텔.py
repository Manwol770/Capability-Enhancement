import sys
input = sys.stdin.readline

K, N = map(int, input().split())
dp = [float('inf')] * (K+102)
dp[0] = 0
for i in range(N):
    v, w = map(int, input().split())
    w_start, w_end = 0, 0
    v1 = 0
    T_F = 0
    for k in range(2, K + 102):
        w_start += w
        w_end = w_start + w
        if w_end > K + 101:
            w_end = K + 101
            T_F = 1
        v1 += v
        for j in range(w_start, w_end):
            dp[j] = min(dp[j], dp[j-w] + v)
        if T_F:
            break

print(min(dp[K:]))