import sys
input = sys.stdin.readline

row, col = map(int, input().split())

matrix = [list(map(int, input().split())) for i in range (row)]

K = int(input())

for tc in range (K) :
    
    x1, y1, x2, y2 = map(int,input().split())
    sum_num = 0

    for i in range (x1-1,x2) :
        for j in range (y1-1,y2) :
            sum_num += matrix[i][j]

    print(sum_num)