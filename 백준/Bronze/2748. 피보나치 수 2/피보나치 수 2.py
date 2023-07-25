import sys
input = sys.stdin.readline

n = int(input())

lst = [0 , 1] + [0]*89

if n >= 2 :
    for i in range (2,n+1) :
        lst[i] = lst[i-1] + lst[i-2]
print(lst[n])