import sys
input = sys.stdin.readline

N = int(input())

Halli = dict()

for i in range(N):

    S ,X = input().split()
    
    if S not in Halli.keys():
        Halli[S] = int(X)
    else:
        Halli[S] = int(Halli[S])+int(X)

if 5 in Halli.values():
    print("YES")
else:
    print("NO")