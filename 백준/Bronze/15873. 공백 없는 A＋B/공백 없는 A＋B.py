n = list(input())

if n[0] == '1' :
    if n[1] == '0' :
        n1 = 10
        n2 = int(''.join(n[2:]))
    else :
        n1 = int(n[0])
        n2 = int(''.join(n[1:]))
else :
    n1 = int(n[0])
    n2 = int(''.join(n[1:]))

print(n1+n2)