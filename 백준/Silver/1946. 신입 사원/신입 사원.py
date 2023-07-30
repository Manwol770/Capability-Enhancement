import sys
input = sys.stdin.readline

Test_case = int(input())
for i in range (Test_case) :

    num = int(input())
    new_employee = []
    for _ in range (num) :
        new_employee.append(list(map(int, input().split())))
    
    new_employee.sort()
    min_rank = new_employee[0][1]
    count = 1

    for j in range (num) :
        real_rank = new_employee[j][1]
        if real_rank < min_rank :
            min_rank = real_rank
            count += 1
    
    print(count)