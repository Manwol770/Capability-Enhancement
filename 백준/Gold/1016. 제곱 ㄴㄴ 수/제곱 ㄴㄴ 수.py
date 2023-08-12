#주어진 최솟값, 최댓값
min_val, max_val = list(map(int, input().split()))

# print(min_val)
# print(max_val)


#최솟값과 최댓값 사이의 값들의 대한 boolean(True) 배열
between_min_max = [True for _ in range(max_val - min_val + 1)]

# print(between_min_num)


#주어진 제한에 의해 제곱수는 2에서 10^6까지 찾아도 됨.
for i in range(2, 10 ** 6 + 1):
    
    #제곱수
    squared = i * i

    #주어진 between_min_num 사이에 있는 제일 첫번째 제곱수 찾기
    first_square = ((min_val + squared - 1) // squared) * squared

    # first_square 부터 squared의 배수는 다 False로 바꾸기
    for j in range(first_square, max_val + 1, squared):
        between_min_max[j - min_val] = False





#출력
print(sum(between_min_max))