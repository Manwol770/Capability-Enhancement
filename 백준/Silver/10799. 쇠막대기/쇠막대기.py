import sys
input = sys.stdin.readline

fe_bar = list(input())
fe_bar.pop()
stn_count = 0
for i in fe_bar :
    stn_count += 1
stack = []
result = 0
for i in range (stn_count) :
    if fe_bar[i] == '(' :
        stack.append(i)
    else :
        stack.pop()
        if fe_bar[i-1] == '(' :
            for i in stack :
                result += 1
        else :
            result += 1
print(result)