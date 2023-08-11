import sys
input = sys.stdin.readline

N = int(input())
sentence_list = list(input())
sentence_list.pop
sum_list = 0
for i in range (N) :
    sum_list += (ord(sentence_list[i])-96)*31**i
print(sum_list%1234567891)