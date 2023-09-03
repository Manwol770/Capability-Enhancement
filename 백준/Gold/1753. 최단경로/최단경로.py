# import sys
# input = sys.stdin.readline
#
# from collections import deque
#
# V, E = map(int, input().split())
# matrix = [[1] for _ in range(V+1)]
# start = int(input())
# visited = [float('inf')] * (V+1)
# visited[start] = 0
# E_set = set()
# removed_list = []
# removed_list_len = 0
#
# for _ in range(E):
#     s, e, w = map(int, input().split())
#     if (s, e) not in E_set:
#         E_set.add((s, e, w))
#         E_set.add((s, e))
#         removed_list.append((s, e))
#         removed_list_len += 1
#     else:
#         for i in range(w+1, 11):
#             if (s, e, i) in E_set:
#                 E_set.remove((s, e, i))
#                 E_set.add((s, e, w))
#
# for i in range(removed_list_len):
#     E_set.remove((removed_list[i][0], removed_list[i][1]))
#
# for s, e, w in E_set:
#     matrix[s].append((e, w))
#     matrix[s][0] += 1
#
# q = deque([start])
#
# while q:
#
#     start = q.popleft()
#     len_start = matrix[start][0]
#
#     for i in range(1, len_start):
#         if visited[matrix[start][i][0]] > matrix[start][i][1] + visited[start]:
#             visited[matrix[start][i][0]] = matrix[start][i][1] + visited[start]
#             q.append(matrix[start][i][0])
#
# for i in range(1, V+1):
#     if visited[i] == float('inf'):
#         print('INF')
#     else:
#         print(visited[i])

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
#시작점 K
K = int(input())
#가중치 테이블 dp
dp = [float('inf')]*(V+1)
heap = []
graph = [[] for _ in range(V + 1)]

def Dijkstra(start):
    #가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(heap,(0, start))

    #힙에 원소가 없을 때 까지 반복.
    while heap:
        wei, now = heapq.heappop(heap)

        #현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플이면 무시.
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            #현재 정점 까지의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W
            # = 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei
            #다음 노드까지의 가중치(next_wei)가 현재 기록된 값 보다 작으면 조건 성립.
            if next_wei < dp[next_node]:
                #계산했던 next_wei를 가중치 테이블에 업데이트.
                dp[next_node] = next_wei
                #다음 점 까지의 가증치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입.
                heapq.heappush(heap,(next_wei,next_node))

#초기화
for _ in range(E):
    u, v, w = map(int, input().split())
    #(가중치, 목적지 노드) 형태로 저장
    graph[u].append((w, v))


Dijkstra(K)
for i in range(1,V+1):
    print("INF" if dp[i] == float('inf') else dp[i])