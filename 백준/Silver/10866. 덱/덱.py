import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
d = deque()
for i in range (N) :
    sentence = deque(map(str, input().split()))
    if sentence[0] == 'push_back' :
        d.appendleft(sentence[1])
    elif sentence[0] == 'push_front' :
        d.append(sentence[1])
    elif sentence[0] == 'front' :
        if d :
            print(d[-1])
        else :
            print(-1)
    elif sentence[0] == 'back' :
        if d :
            print(d[0])
        else :
            print(-1)
    elif sentence[0] == 'size' :
        print(len(d))
    elif sentence[0] == 'empty' :
        if d :
            print(0)
        else :
            print(1)
    elif sentence[0] == 'pop_front' :
        if d :
            print(d.pop())
        else :
            print(-1)
    elif sentence[0] == 'pop_back' :
        if d :
            print(d.popleft())
        else :
            print(-1)