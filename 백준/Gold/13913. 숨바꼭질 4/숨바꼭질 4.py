import sys

input = sys.stdin.readline

N, K = map(int, input().split())

max_num = max(N, K)

arr = [0] * (max_num + 2)
visited = [0] * (max_num + 2)

delta = [1, -1, 2]

count = 1
stack = [N]
visited[N] = 1
arr[N] = 0
path = [0] * (max_num + 2)

while stack:

    x = stack.pop(0)

    for i in range(1, 4):
        if i % 3 == 0:
            nx = x * delta[i - 1]
        else:
            nx = x + delta[i - 1]

        if 0 <= nx < max_num + 2 and visited[nx] == 0:
            visited[nx] = 0
            arr[nx] = arr[x] + 1
            visited[nx] = 1
            stack.append(nx)
            path[nx] = x
print(arr[K])
len_K = arr[K]
print_list = [K]
while K != N:
    K = path[K]
    print_list.append(K)
for i in range(len_K, -1, -1):
    print(print_list[i], end=' ')