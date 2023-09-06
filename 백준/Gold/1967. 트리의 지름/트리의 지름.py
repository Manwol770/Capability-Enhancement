import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(N, r):
    global max_num

    if Tree_ch[N] and not visited[Tree_ch[N][0]]:
        visited[Tree_ch[N][0]] = 1
        dfs(Tree_ch[N][0], r + Tree_ch[N][1])
    if Tree_p[N]:
        T = len(Tree_p[N])
        for j in range(T):
            if not visited[Tree_p[N][j][0]]:
                visited[Tree_p[N][j][0]] = 1
                dfs(Tree_p[N][j][0], r + Tree_p[N][j][1])
            else:
                max_num = max(max_num, r)
        else:
            max_num = max(max_num, r)
    else:
        max_num = max(max_num, r)

N = int(input())
Tree_p = [[] for _ in range(N+1)]
Tree_ch = [0] * (N+1)
for i in range(N-1):
    p, ch, val = map(int, input().split())
    Tree_p[p].append((ch, val))
    Tree_ch[ch] = (p, val)

max_num = 0

for i in range(1, N+1):
    if not Tree_p[i] :
        visited = [0] * (N+1)
        visited[i] = 1
        dfs(i, 0)

print(max_num)