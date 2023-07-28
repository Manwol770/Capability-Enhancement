#코드를 입력하세요.
import sys

x = int(input())

for i in range(x):
    P_wants = []
    count = 0
    P, M = map(int, input().split())
    for i in range(P):
        P_wants.append(int(input()))
    if M == 1:                          # 자리가 한개일때
        print(P - 1)
    else:
        count = 0
        for i in range(1, M+1):
            if P_wants.count(i) >= 2:      # 동일 자리가 2개 이상일때
                count += P_wants.count(i) - 1
        print(count)