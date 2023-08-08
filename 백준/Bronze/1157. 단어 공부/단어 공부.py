x = input().upper()
N = []

for Y in range (65,91) :
    N.append(0)

for X in range (len(x)) :
    for Y in range (65,91) :
        if ord(x[X]) == Y :
            N[Y-65] += 1


if N.count(max(N)) > 1 :
    print("?")
else :
    print(f"{chr(N.index(max(N))+65)}")