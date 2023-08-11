import sys
input = sys.stdin.readline

N,r,c = map(int, input().split())

row = N
col = N
sum_num = 0

while row != -1 :
    if 1<<row > r :
        row -= 1
        continue
    sum_num += 2*4**row
    r -= 1<<row
    row -= 1

while col != -1 :
    if 1<<col > c :
        col -= 1
        continue
    sum_num += 4**col
    c -= 1 << col
    col -= 1

print(sum_num)