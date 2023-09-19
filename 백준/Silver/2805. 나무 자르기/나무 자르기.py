import sys
input = sys.stdin.readline


N, M = map(int, input().split())
N_list = list(map(int, input().split()))
end = max(N_list)
start = 1

while start <= end:
    middle = (start + end) // 2
    tree = 0
    for i in N_list:
        if i > middle:
            tree += (i-middle)

    if tree >= M:
        start = middle + 1

    else:
        end = middle - 1

print(end)