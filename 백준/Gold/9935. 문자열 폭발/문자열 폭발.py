import sys
input = sys.stdin.readline


sentence = list(input().strip())
boom_sentence = list(input().strip())
sentence_cnt = 0
sentence_len = len(sentence)
boom_sentence_len = len(boom_sentence)

stack = []

for i in range(sentence_len):
    if sentence_cnt >= boom_sentence_len-1:
        if sentence[i] == boom_sentence[boom_sentence_len - 1]:
            for j in range(1, boom_sentence_len):
                if stack[sentence_cnt-j] != boom_sentence[boom_sentence_len - j - 1]:
                    stack.append(sentence[i])
                    sentence_cnt += 1
                    break
            else:
                for j in range(boom_sentence_len - 1):
                    stack.pop()
                    sentence_cnt -= 1
        else:
            stack.append(sentence[i])
            sentence_cnt += 1
    else:
        stack.append(sentence[i])
        sentence_cnt += 1

if stack:
    print(''.join(stack))
else:
    print("FRULA")