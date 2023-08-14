import sys
input = sys.stdin.readline

T = int(input())
for i in range (1, T+1) :
    N = int(input())
    dp = [1, 2, 4, 7]
    for i in range (4,N) :
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[N-1])