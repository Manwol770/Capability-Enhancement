import sys
input = sys.stdin.readline
from collections import deque

arr = [x for x in range (0,100)]
visited = [0]*100
arr1 = [float('inf')]*100
N, M = map(int, input().split())

for i in range (N+M) :
    num1, num2 = map(int, input().split())
    arr[num1-1] = num2 - 1

delta = [6,5,4,3,2,1]
stack = deque([0])
arr1[0] = 0
visited[0] = 1

while stack :

    n = stack.popleft()
    
    for i in range (6) :
        next_n = n + delta[i]
        if 0 <= next_n < 100 and visited[next_n] == 0 :
            visited[next_n] = 1
            arr1[next_n] = min(arr1[next_n], arr1[n] + 1)
            next_n = arr[next_n]
            visited[next_n] = 1
            arr1[next_n] = min(arr1[next_n], arr1[n] + 1)
            stack.append(next_n)
print(arr1[99])