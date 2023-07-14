import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = 0
c = 0

for k in range (5) :
    b = a[k]
    c += b**2
    
print(c%10)