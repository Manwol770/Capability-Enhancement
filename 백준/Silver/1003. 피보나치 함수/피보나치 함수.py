import sys
input = sys.stdin.readline

T = int(input())
for tc in range (1,T+1) :
    N = int(input())
    dp = [0,1]
    if N > 1 :
        for i in range (2,N+1) :
            dp.append(dp[i-1]+dp[i-2])
    if not N :
        print(dp[N+1], dp[N])
    else :
        print(dp[N-1],dp[N])