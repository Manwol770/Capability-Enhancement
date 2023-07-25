N = int(input())
compare_num = 0
three_six_num = 0

while compare_num != N :
    three_six_num += 1
    if '666' in str(three_six_num) :
        compare_num += 1

print(three_six_num)