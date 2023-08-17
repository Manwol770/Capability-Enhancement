import sys
import math

M, N = map(int, sys.stdin.readline().split())

numbers = []
for _ in range(M):
    numbers.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))

result = -1

for m in range(M):
    for n in range(N):
        for weight_m in range(-M, M):
            for weight_n in range(-N, N):

                if weight_m == 0 and weight_n == 0: continue
                step = 0
                x = m
                y = n
                value = ''

                while (0 <= x < M) and (0 <= y < N):
                    value += str(numbers[x][y])
                    step += 1

                    value_int = int(''.join(value))
                    value_sqrt = math.sqrt(value_int)
                    value_decimal = value_sqrt - int(value_sqrt)
                    if value_decimal == 0 and value_int > result: result = value_int

                    x = m + step * weight_m
                    y = n + step * weight_n

print(result)