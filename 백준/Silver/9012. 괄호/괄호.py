import sys
input = sys.stdin.readline

num = int(input())

print_list = []

for i in range (0,num) :
    word = list(map(str,str(input())))
    word.pop()
    str_word = ''.join(word)
    while '()' in str_word :
        str_word = str_word.split('()')
        str_word = ''.join(str_word)
    
    if str_word == '' :
        print_list.append('YES')
    else :
        print_list.append('NO')

for i in print_list :
    print(i)