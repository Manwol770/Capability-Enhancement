import sys
input = sys.stdin.readline

# #파도반 함수
# def padoban(n) :
#     #초기 값
#     if n <= 3 :
#         return 1
#     #이후 값
#     else :
#         n = padoban(n-2)+padoban(n-3)
#         return n

# #테스트 숫자
# Test_case_num = int(input())

# #테스트 숫자만큼 숫자 받아서 파도반 함수 돌리기
# for num in range (Test_case_num) :
#     print(padoban(int(input())))

#---------시간 초과로 다시-----------

#테스트 케이스 숫자
case_num = int(input())

#테스트 케이스 만큼 for문
for num in range (case_num) :
    #초기값
    padoban_list = [1,1,1]

    #파반느 N값까지 리스트 만들기
    test_num = int(input())
    
    if test_num > 3 :
        for num in range (3,test_num) :
            padoban_list.append(padoban_list[num-2] + padoban_list[num - 3])
    
    #파반느 N값 출력
    print(padoban_list[test_num-1])