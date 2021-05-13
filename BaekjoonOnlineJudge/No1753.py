# 방향그래프가 주어지고,
# 시작점에서 다른 모든 정점으로의 최단 경로를 구하기

import sys
from heapq import heappush, heappop

INF = 100000000

# 정점의 개수 v, 간선의 개수 e
v, e = map(int, sys.stdin.readline().split())

# 시작 정점의 번호
k = int(sys.stdin.readline())

matrix = [[] for _ in range(v+1)]

dp = [INF]*(v+1)

heap = []

def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in matrix[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    # u에서 v로 가는 가중치 w인 간선이 존재
    matrix[u].append([v, w])

dijkstra(k)

for i in dp[1:]:
    print(i if i != INF else "INF")