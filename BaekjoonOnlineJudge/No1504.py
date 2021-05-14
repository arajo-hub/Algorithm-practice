from heapq import heappush, heappop
import sys

# 정점의 개수 n, 간선의 개수 e
n, e = map(int, sys.stdin.readline().split())

matrix = [[] for i in range(n+1)]

INF = sys.maxsize

for _ in range(e):
    # a번 정점에서 b번 정점까지의 거리가 c
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append([b, c])
    matrix[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    dp = [INF for i in range(n+1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, c = heappop(heap)
        for n_n, n_w in matrix[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heappush(heap, [wei, n_n])
    return dp

one = dijkstra(1)
v1_result = dijkstra(v1)
v2_result = dijkstra(v2)
count = min(one[v1] + v1_result[v2] + v2_result[n], one[v2] + v2_result[v1] + v1_result[n])
print(count if count < INF else -1)