
import sys
input = sys.stdin.readline

def collection(cnt, s, k):
    global result

    if cnt == s:
        select_bbq_list = []
        for i in range(bbq_len):
            if bbq_list[i] == 1:
                select_bbq_list.append(bbq[i])
        line_sum = 0
        for i in range(house_len):
            min_line = float('inf')
            v1 = house[i][0]
            w1 = house[i][1]
            for j in range(K):
                v2 = select_bbq_list[j][0]
                w2 = select_bbq_list[j][1]
                min_line = min(min_line, abs(v1-v2) + abs(w1-w2))
            line_sum += min_line
            if line_sum > result:
                return
        result = min(result, line_sum)
        return

    if bbq_len == k:
        return

    bbq_list[k] = 1
    collection(cnt + 1, s, k + 1)
    bbq_list[k] = 0
    collection(cnt, s, k + 1)



N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range (N)]

house = []
house_len = 0
bbq = []
bbq_len = 0
result = float('inf')

for i in range (N):
    for j in range(N):
        if matrix[i][j] == 2:
            bbq.append((i, j))
            bbq_len += 1
        elif matrix[i][j] == 1:
            house.append((i, j))
            house_len += 1

bbq_list = [0]*(bbq_len)
collection(0, K, 0)
print(result)