import sys
input = sys.stdin.readline

#준규의 카드 갯수를 받음
N = int(input())
#준규의 카드 숫자들 받을 딕셔너리를 생성
card_dict = {}

for _ in range (N) :
    #카드의 적힌 정수를 보고 카드 갯수를 세주는 for문
    card_num = input()
    if card_num in card_dict :
        card_dict[f'{card_num}'] += 1
    else :
        card_dict[f'{card_num}'] = 1

#초기값 설정 문제에서 주어지는 정수는 2**62보다 낮음
row_card_mum,high_card_dict_val = 2**62,0

#카드 갯수가 최고 숫자인지 판별하고
#가장 많은 숫자를 가진 카드중에서 정수가 가장 낮은걸 골라주는 for문
for dict_key in card_dict :
    if high_card_dict_val < card_dict[f'{dict_key}'] :
        high_card_dict_val = card_dict[f'{dict_key}']
        row_card_mum = int(dict_key)
    elif high_card_dict_val == card_dict[f'{dict_key}'] :
        if row_card_mum > int(dict_key) :
            row_card_mum = int(dict_key)

print(row_card_mum)