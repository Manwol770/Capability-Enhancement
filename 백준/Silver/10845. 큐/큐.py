import sys
input = sys.stdin.readline

num = int(input())
num_list = []
sentece_list = []
for i in range (num) :
    sentece_list = list(map(str, input().split()))
    if sentece_list[0] == 'push' :
        num_list.append(sentece_list[1])
    elif sentece_list[0] == 'front' :
        if len(num_list) :
            print(num_list[0])
        else :
            print(-1)
    elif sentece_list[0] == 'back' :
        if len(num_list) :
            print(num_list[-1])
        else :
            print(-1)
    elif sentece_list[0] == 'pop' :
        if len(num_list) :
            print(num_list.pop(0))
        else :
            print(-1)
    elif sentece_list[0] == 'empty' :
        if len(num_list) :
            print(0)
        else :
            print(1)
    else :
        print(len(num_list))