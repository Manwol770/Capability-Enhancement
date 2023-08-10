def reflection(n) :
    if n == 1 or n == 2 :
        return 1
    return (reflection(n-1) + reflection(n-2))

def dp (n) :
    global dp_cnt
    dp = [0,1]
    if n >= 2 :
        for i in range (2,n) :
            dp_cnt += 1
            dp.append(dp[i-1] + dp[i-2])
    return None


N = int(input())
dp_cnt = 0
dp(N)
print(reflection(N), dp_cnt)