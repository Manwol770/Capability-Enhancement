import sys
input = sys.stdin.readline

num1, num2 = map(int,input().split())

sentence_set1 = set()
sentence = ''
count = 0

for i in range (num1) :
    sentence_set1.add(input().rstrip('\n'))

for j in range (num2) :
    sentence = input().rstrip('\n')
    if sentence in sentence_set1 :
        count += 1

print(count)