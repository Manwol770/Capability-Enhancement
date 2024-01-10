import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(0, N):
        if( i + j < N + 1 and dp[i + j] < dp[j] + array[i - 1] ):
            dp[i + j] = dp[j] + array[i - 1]

print(dp[N])