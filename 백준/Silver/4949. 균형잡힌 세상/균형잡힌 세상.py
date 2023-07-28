import sys
input = sys.stdin.readline

while True :
    setence = input()

    if setence == '.\n' :
        break

    s_list = []

    for i in setence :
        if i == '(' or i == ')' or i == '[' or i == ']' :
            s_list.append(i)

    s_list = ''.join(s_list)

    for i in range (len(s_list)) :

        k = len(s_list)

        s_list = s_list.split('()')
        s_list = ''.join(s_list)
        s_list = s_list.split('[]')
        s_list = ''.join(s_list)

        if k == len(s_list) :
            break

    if s_list == '' :
        print('yes')
    else :
        print('no')