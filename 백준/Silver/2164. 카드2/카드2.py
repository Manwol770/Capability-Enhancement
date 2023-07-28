import sys
input = sys.stdin.readline

num = int(input())
two_num = 0
n = num

while True :

    if int(num/2) < 1 :
        break 
    num = num/2
    two_num += 1


if n == 1 :
    m = 1

elif n / 2**two_num == 1 :
    m = n

else :
    m = 2 * (n - 2**two_num)

print(m)