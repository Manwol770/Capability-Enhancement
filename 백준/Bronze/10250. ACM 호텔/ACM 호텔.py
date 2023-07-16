import sys
input = sys.stdin.readline

a = int(input())
b,c = 0,0

d = []

for _ in range (a) :
    x,y,z = map(int, input().split())
    if (z % x) == 0 :
        c = z//x
        d.append(x*100+c)
    else :
        b = z%x
        c = z//x+1
        d.append(b*100+c)

for k in range (a) :
    print(d[k], end = "\n")