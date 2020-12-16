# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# for tc in range(int(input())):
#     n = int(input())

#     graph = []
#     for i in range(n):
#         graph.append(list(map(int, input().split())))

#     distance = [[INF] * n for _ in range(n)]

#     x, y = 0, 0
#     q = [(graph[x][y], x, y)]
#     distance[x][y] = graph[x][y]

#     while q:
#           dist, x, y = heapq.heappop(q)
#           if distance[x][y] < dist:
#               continue
#           for i in range(4):
#               nx = x + dx[i]
#               ny = y + dy[i]
#               if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                   continue
#               cost = dist + graph[nx][ny]
#               if cost < distance[nx][ny]:
#                   distance[nx][ny] = cost
#                   heapq.heappush(q, (cost, nx, ny))

#     print(distance[n-1][n-1])

# 2020년 12월 16일 풀이

import heapq
import sys

INF=int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    array=[]
    for i in range(n):
        array.append(list(map(int, sys.stdin.readline().split())))
        distance=[[INF]*n for _ in range(n)]
    x, y=0, 0
    q=[(array[x][y], x, y)]
    distance[x][y]=array[x][y]
    
    while q:
            dist, x, y = heapq.heappop(q)
            if distance[x][y] < dist:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                cost = dist + array[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n-1][n-1])