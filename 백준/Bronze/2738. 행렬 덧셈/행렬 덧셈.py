rows,columns = map(int, input().split())

A = []
B = []
C = []

count = 0

plus_list = []

for i in range(rows) :
    plus_list = list(map(int, input().split()))
    A.append(plus_list)

for j in range(rows) :
    plus_list = list(map(int, input().split()))
    B.append(plus_list)

for i in range(rows) :
    plus_list = []
    for j in range(columns) :
        plus_list.append(A[i][j]+B[i][j])
    C.append(plus_list)

for i in range (rows) :
    for j in range (columns) :
        print(C[i][j], end = ' ')
    print('')