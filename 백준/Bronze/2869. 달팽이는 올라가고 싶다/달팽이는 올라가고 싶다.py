x,y,z = map(int,input().split())
day = 1

k = x-y
l = z-x
n = l/k
if n != int(n) :
    n += 1

print(int(n)+day)