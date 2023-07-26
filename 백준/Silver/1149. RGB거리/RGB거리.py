num = int(input())

cost = [[0,0,0]]
for j in range (0,num) :
    cost.append(list(map(int, input().split())))

dp = [[float('inf'),float('inf'),float('inf')] for _ in range (num+1)]
color = [0]*num
dp[0] = [0,0,0]

dp[1] = cost[1]

for i in range (0,num) :
    for j in range (0,3) :
        for k in range (0,3) :
            if j != k  :
                dp[i+1][j] = min(dp[i+1][j], cost[i+1][j] + dp[i][k])

print(min(dp[num]))