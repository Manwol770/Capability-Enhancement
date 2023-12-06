import heapq
k, n = map(int, input().split())
prime = list(map(int, input().split()))
heap = [] # 최소힙

for idx, p in enumerate(prime): # 주어진 소수들을 힙에 추가한다.
    heapq.heappush(heap,(p, idx)) # 값, 초기 소수의 인덱스


for i in range(n): # 힙의 n번째 원소 출력

    # 힙에서 제일 작은 값과 그 값을 만들어낸 초기 소수의 인덱스를 꺼낸다.
    min_number, base_idx = heapq.heappop(heap)

    for idx, p in enumerate(prime):
        
        # 초기 소수의 다음 소수부터는 곱하지 않는다. (중복 방지)
        if idx > base_idx:
            break

        # 힙에서 꺼낸 제일 작은 원소에 소수를 차례대로 하나씩 곱한다.
        new_number = p * min_number
        
        # 만든 새 숫자를 힙에 추가한다.
        heapq.heappush(heap, (new_number, idx))


    if i == n-1:
        print(min_number)