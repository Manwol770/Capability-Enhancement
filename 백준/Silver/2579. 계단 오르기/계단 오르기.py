import sys
input = sys.stdin.readline
arr = []
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))


dp.append(arr[0])
if l > 1 :
    dp.append(arr[0]+arr[1])
if l > 2 :
    dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))
if l > 3 :
    for i in range(3,l):
        dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

print(dp[l-1])