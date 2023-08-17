n,m = int(input()), 1

while True :
    if 1<<m >= 2 * n :
        break
    m += 1

print(2*n-2**(m-1))