import sys
input = sys.stdin.readline

num = int(input())
for i in range (num) :
    str_ = list(map(str,str(input())))
    str_.pop()
    print(str_[0]+str_[-1])