import sys
input = sys.stdin.readline

S = int(input().strip())
lis = list(input().strip())
p_lis = []
c_lis = []

for i in range(S):
    if lis[i] == 'P':
        p_lis.append(i)
    elif lis[i] == 'C':
        c_lis.append(i)
    else:
        continue
for i in range(len(p_lis)):
    if i > len(c_lis) - 1:
        break
    lis[p_lis[i]] = 'C'

for i in range(len(c_lis)):
    if i > len(p_lis) - 1:
        break
    lis[c_lis[i]] = 'P'

print(''.join(lis))