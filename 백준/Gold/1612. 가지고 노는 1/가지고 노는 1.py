import sys
input = sys.stdin.readline

def one_distinguish(num) :

    one_OK = ['1','3','7','9']

    if str(num)[-1] in one_OK :
        return num
    else :
        return -1
    

num = int(input())
num_list = []
test_str = ''
a = 0
b = 0
num = one_distinguish(num)
num_count = -1

if num != -1 :
    num_count = 0
    while True :

        a += 1
        str_num = str(a*num+b)

        if str_num[-1] == '1' :

            a = 0
            num_list = list(str_num[:-1])

            test_str = ''.join(num_list)
            num_count += 1

            if test_str.strip('1') == '' :
                num_count += len(test_str)
                break

            b = int(test_str)
            

        else :
            continue

print(num_count)