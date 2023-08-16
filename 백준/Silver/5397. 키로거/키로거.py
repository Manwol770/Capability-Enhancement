import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    password = []
    password2 = []
    sentence = input().rstrip()
    for i in sentence:
        if i == '-':
            if password: 
                password.pop()
        elif i == '<': 
            if password:
                password2.append(password.pop())
        elif i == '>': 
            if password2:
                password.append(password2.pop())
        else:
            password.append(i)
    password.extend(reversed(password2))
    print(''.join(password))