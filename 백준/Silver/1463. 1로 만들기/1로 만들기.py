import sys
input = sys.stdin.readline

num = int(input())

dp = [0] * 2 + [float('inf')] * (num-1)

for i in range (1, num + 1) :
    if i % 6 == 0 :
        dp[i] = min(dp[i], dp[int(i/2)] + 1, dp[int(i/3)] + 1, dp[i-1] + 1)
    elif i % 2 == 0 :
        dp[i] = min(dp[i], dp[int(i/2)] + 1, dp[i-1] + 1)
    elif i % 3 == 0 :
        dp[i] = min(dp[i], dp[int(i/3)] + 1, dp[i-1] + 1)
    else :
        dp[i] = min(dp[i],dp[i-1] + 1)

print(dp[num])