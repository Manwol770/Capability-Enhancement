N,C,W = map(int,input().split())
dp = [[1]]
for i in range (1,N+W) :
    triangle = []
    for j in range (i+1) :
        if j == 0 :
            triangle.append(dp[i-1][j])
        elif j == i :
            triangle.append(dp[i-1][j-1])
        else :
            triangle.append(dp[i-1][j-1]+dp[i-1][j])
    dp.append(triangle)
sum_num = 0
high = 0
for i in range (N-1,N+W-1) :
    high += 1
    for j in range (high) :
        sum_num += dp[i][C-1+j]
print(sum_num)