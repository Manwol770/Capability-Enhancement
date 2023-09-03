import sys
input = sys.stdin.readline
n = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
count = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

def solve(x, y, dir):
    tmp = 0

    if x == n-1 and y == n-1:
        count[x][y][dir] = 1
        return count[x][y][dir]

    if count[x][y][dir] != -1:
        return count[x][y][dir]

    # 오른쪽으로 가려고 하는 경우
    if dir <= 1 and y + 1 < n and graph[x][y+1] != 1:
        tmp += solve(x, y+1, 0)

    # 대각선으로 가려고 하는 경우
    if x + 1 < n and y + 1 < n and \
        graph[x][y+1] != 1 and graph[x+1][y] != 1 and graph[x+1][y+1] != 1:
        tmp += solve(x+1, y+1, 1)

    # 아래쪽으로 가려고 하는 경우
    if dir >= 1 and x + 1 < n and graph[x+1][y] != 1:
        tmp += solve(x+1, y, 2)

    count[x][y][dir] = tmp
    return count[x][y][dir]

print(solve(0,1,0))

# -> : 0
# ┘  : 1
# v  : 2