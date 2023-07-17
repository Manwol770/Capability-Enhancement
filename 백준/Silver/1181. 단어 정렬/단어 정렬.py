num = int(input())

sentence = []

for _ in range (num) :
    sentence.append(input())

sentence = set(sentence)
sentence = list(sentence)

sentence.sort()
sentence.sort(key=len)

for a in range (len(sentence)):
    print(sentence[a])