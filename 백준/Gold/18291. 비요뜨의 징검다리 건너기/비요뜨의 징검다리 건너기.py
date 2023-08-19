import sys
input = sys.stdin.readline

T = int(input())

for tc in range (T) :

    n = int(input())

    def power(one, two):
        return (one * two) % 1000000007

    def solve(n):
        if n == 1:
            return 2

        part = solve(n//2)
        answer = power(part, part)

        if n%2:
            return answer * 2
        else:
            return answer

    if n<=2:
        print(1)
    else:
        print(solve(n-2) % 1000000007)