import sys
input = sys.stdin.readline

# 막대기 수 받기
N = int(input())

# 보이는 막대 리스트
see_bar_list = []
# 막대 숫자 리스트
Num_list = []
#막대가 보이는지 구분해줄 숫자
high_Num = 0

for _ in range (N) :

    #막대 숫자를 받아서 리스트에 추가
    bar_num = int(input())
    Num_list.append(bar_num)

for Num in Num_list[::-1] :
    if high_Num < Num :
        high_Num = Num
        see_bar_list.append(high_Num)

print(len(see_bar_list))