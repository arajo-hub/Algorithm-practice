import sys

v, e = map(int, sys.stdin.readline().split())

INF = 100000000
matrix = [[INF] * v for _ in range(v)]

for i in range(e):
    # a 마을에서 b 마을로 가는 거리가 c
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a - 1][b - 1] = c

for k in range(v): # 중간에 거쳐갈 마을 하나 정하고
    for i in range(v): # 출발지 마을 하나 정하고
        for j in range(v): # 도착지 마을 하나 정하고
            # 최단거리 찾기
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

result = INF

for i in range(v):
    result = min(result, matrix[i][i])

if result == INF:
    print(-1)
else:
    print(result)

# 하나의 정점에서 출발해서 다른 모든 정점으로의 최단 경로를 구할 때는 다익스트라 알고리즘.
# 모든 정점에서 모든 정점으로의 최단 경로를 구하고 싶다면 플로이드 와샬 알고리즘.