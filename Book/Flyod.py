# import sys

# INF=int(1e9)

# N=int(sys.stdin.readline())
# M=int(sys.stdin.readline())

# graph=[[INF]*(N+1) for _ in range(N+1)]

# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if a==b:
#             graph[a][b]=0 # 도시의 출발지와 목적지가 같은 경우는 0

# for _ in range(M):
#     a, b, c=map(int, input().split())
#     if c<graph[a][b]:
#         graph[a][b]=c # 버스의 정보 입력(a도시에서 b도시까지 가는 데 필요한 비용 c)

# for k in range(1, N+1):
#     for a in range(1, N+1):
#         for b in range(1, N+1):
#             graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
#             # a부터 k까지 갔다가 k에서 b로 가는 비용과
#             # a에서 b로 가는 비용 중 적은 비용을 저장한다.

# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if graph[a][b]==INF: # 갈 수 없는 경우는 0 출력
#             print(0, end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()

# 2020년 12월 14일 풀이

import sys

INF=int(1e9)

n=int(sys.stdin.readline()) # 도시의 개수
m=int(sys.stdin.readline()) # 버스의 개수

graph=[[INF]*(n+1) for _ in range(n+1)] # 전부 INF로 채우고

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b]=0 # 움직이지 않는 경우는 0

for _ in range(m):
    # 버스의 출발 도시 a, 도착 도시 b, 한 번 타는 데 필요한 비용 c
    a, b, c=map(int, sys.stdin.readline().split())
    if c<graph[a][b]:
        graph[a][b]=c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
            # a에서 b로 가는 비용은
            # 1. a에서 b로 가는 비용 과
            # 2. a에서 k로 갔다가 k에서 b로 가는 비용 중 더 싼 비용으로.

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b]==INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()