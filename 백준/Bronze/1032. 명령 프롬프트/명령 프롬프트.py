import sys
input = sys.stdin.readline

T = int(input())
print_text = list(input().strip())
for i in range(T - 1):
    text = list(input().strip())
    for j in range(len(print_text)):
        if print_text[j] == '?':
            continue
        elif print_text[j] == text[j]:
            continue
        else:
            print_text[j] = '?'

print(''.join(print_text))