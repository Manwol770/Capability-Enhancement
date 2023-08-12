import sys
input = sys.stdin.readline

formula = input()
int_stack = []
stack = []
cnt = 0
max_cnt = len(formula)

sum_num = 0
for i in formula :
    if i == '+' :
        sum_num += int(''.join(int_stack))
        int_stack = []
        cnt += 1
    elif i == '-' :
        sum_num += int(''.join(int_stack))
        int_stack = []
        cnt += 1
        break
    else :
        int_stack.append(i)
        cnt += 1
else :
    sum_num += int(''.join(int_stack))
    int_stack = []

for i in range (cnt, max_cnt) :
    if formula[i] == '+' or formula[i] == '-' :
        sum_num -= int(''.join(int_stack))
        int_stack = []
    else :
        int_stack.append(formula[i])
else :
    if int_stack :
        sum_num -= int(''.join(int_stack))

print(sum_num)