num = int(input())


if num > 5 :
    dp = [0] + [float('inf')] * num
    dp[3] = 1
    for i in range (5,num+1) :
        dp[i] = min(dp[i], dp[i-3] + 1, dp[i-5] + 1)
else :
    dp = [0,0,0,1,0,1]

if dp[num] == float('inf') or dp[num] == 0 :
    dp[num] = -1

print(dp[num])