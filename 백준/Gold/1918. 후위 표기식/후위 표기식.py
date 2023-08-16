import sys
input = sys.stdin.readline

icp = {'(' : 3, '*':2 , '/':2, '+':1 , '-':1}
isp = {'(' : 0, '*':2, '/' : 2 , '+' : 1, '-' : 1}
# 주어진 계산식
sentence_middle = input().rstrip()
# 후위표기식 담을 문자열
sentence_back = ''
# 후위 표기식으로 바꾸는 과정에 필요한 스택 생성
stack = []

# 1. 후위표기식으로 바꾸기
for x in sentence_middle:

    if x not in '(+-*/)':
        sentence_back += x
    elif x == ')' :
        while stack[-1] != '(':
            sentence_back += stack.pop()
        stack.pop()
    else :
        while stack and isp[stack[-1]] >= icp[x]:
            sentence_back += stack.pop()
    # 우선순위가 더 높다면
        stack.append(x)

# 모든 과정 후에 스택에 남아있다면
while stack:
    # pop해서 추가
    sentence_back += stack.pop()

print(sentence_back)