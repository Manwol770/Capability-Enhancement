a, b = map(int, input().split())
psum = [0 for x in range(60)]

for i in range(1, 60):
    psum[i] = 2**(i-1) + 2 * psum[i-1]

def check(num):
    count = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)

    for i in range(length):
        if bin_num[i] == '1':
            # pow : num 보다 크지 않으면서 가장 큰 2의 거듭제곱 수의 제곱 수
            pow = length-i-1
            # psum[pow] : num 보다 작은 자리수를 가진 수들의 1을 모두 카운트한 수
            count += psum[pow]
            # 가장 앞자리 1 개수를 세서 추가
            count += (num - 2 ** pow + 1)
            num = num - 2 ** pow
    return count

print(check(b) - check(a-1))