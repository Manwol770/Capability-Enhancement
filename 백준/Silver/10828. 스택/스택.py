import sys
input=sys.stdin.readline
n = int(input())

aa = []

for i in range (n):
    ary = list(map(str,input().split()))

    if ary[0] == 'push' :
        aa.append(ary[1])
        
    elif ary[0] == 'pop' :
        if len(aa) == 0 :
            print(-1)
        else :
            print(aa.pop())
    
    elif ary[0] == 'size' :
        print(len(aa))
    
    elif ary[0] == 'empty' :
        if len(aa) == 0 :
            print(1)
        else :
            print(0)
    
    elif ary[0] == 'top' :
        if len(aa) == 0 :
            print(-1)
        else :
            print(aa[-1])