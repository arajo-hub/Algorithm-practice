# import heapq
# import sys

# n, m=map(int, sys.stdin.readline().split())
# INF=int(1e9)
# graph=[[] for _ in range(n+1)]
# distance=[INF]*(n+1)
# start=1 # 첫번째 헛간에서 시작

# for i in range(m):
#     a, b=map(int, sys.stdin.readline().split())
#     graph[a].append((b, 1)) # a번 헛간과 연결된 헛간번호와 이동비용을 graph의 a번째 칸에 추가해준다.
#     graph[b].append((a, 1)) # b번 헛간에도 연결된 헛간번호와 이동비용을 graph의 b번째 칸에 추가해준다.

# def dijkstra(start):
#     q=[]
#     heapq.heappush(q, (0, start)) # q에 (최단거리(=최소이동비용), 현재위치) 이런 식으로 추가
#     distance[start]=0
#     while q:
#         dist, now=heapq.heappop(q)
#         if distance[now]<dist: # 현재위치의 거리가 최단거리보다 작다면 continue
#             continue
#         for j in graph[now]: # 현재위치에서 갈 수 있는 (헛간번호, 이동비용)(=j)을 꺼내서
#             cost=dist+j[1] # 이동비용에 그 이동비용을 추가해주고
#             if cost<distance[j[0]]: # 만약 그렇게 바뀐 새 이동비용이 새 헛간(j[0])까지의 이동비용보다 작다면
#                 distance[j[0]]=cost # 더 작은 값으로 바꿔준다.
#                 heapq.heappush(q, (cost, j[0])) # 그리고 q에 바뀐 값들을 추가해준다.

# dijkstra(start)

# max_node=0
# max_distance=0
# result=[]

# for k in range(1, n+1):
#     if max_distance<distance[k]: # k번째 헛간까지 가는 거리가 max_distance보다 크다면
#         max_node=k # 최단거리가 가장 먼 헛간번호를 k로 넣어준다.
#         max_distance=distance[k] # 그리고 max_distance에 k까지 가는 거리를 넣어준다.
#         result=[max_node] # result에는 최단거리가 가장 먼 헛간번호가 담기게 된다.
#     elif max_distance==distance[k]: # k번째 헛간까지의 거리와 max_distance가 같다면
#         result.append(k) # result에 넣어준다.

# print(max_node, max_distance, len(result))

# 2020년 12월 17일 풀이

import heapq
import sys

n, m=map(int, sys.stdin.readline().split()) # 헛간의 개수 n, 양방향 통로의 개수 m

INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
start=1

for i in range(m):
    a, b=map(int, sys.stdin.readline().split()) # 서로 연결된 두 헛간의 번호
    graph[a].append((b, 1)) # a가 b번 헛간과 연결되어 있는데 그 이동비용이 1이라는 의미.
    graph[b].append((a, 1)) # b가 어떤 헛간과 연결되어 있는데 그 이동비용이 1이라는 의미.

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start)) # q에 (최소이동비용, 시작점)을 넣는다.
    distance[start]=0 # 시작점의 최소이동비용은 0.
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist: # 이동비용이 현재 위치의 거리보다 크다면
            continue # 그냥 지나간다.
        # 이동비용이 현재 위치의 거리보다 작다면!
        for j in graph[now]: # 현재 헛간과 연결되어있는 헛간들을 차례로 꺼낸다. (헛간번호, 최소이동비용)
            # 현재 헛간에서 연결된 헛간으로 갔다고 가정하고 보면 쉬움!
            cost=dist+j[1] # 총비용은 q에서 꺼낸 거리에 현재 헛간과 연결되어있는 헛간 하나의 최소이동비용을 더한 것.
            if cost<distance[j[0]]: # 만약 cost가 현재 헛간과 연결된 헛간으로 이동하는 거리보다 작다면
                distance[j[0]]=cost # 그 값을 cost로 바꿔주고
                heapq.heappush(q, (cost, j[0])) # q에다가 넣어준다.

dijkstra(start)

max_node=0 # 최단거리가 가장 먼 헛간 번호
max_distance=0 # 최장거리
result=[] # 최장거리의 헛간과 같은 거리를 갖는 헛간을 넣을 리스트.

for k in range(1, n+1):
    if max_distance<distance[k]: # k번째 헛간까지 가는 거리가 max_distance보다 크다면
        max_node=k # 최단거리가 가장 먼 헛간번호를 k로 넣어준다.
        max_distance=distance[k] # 그리고 max_distance에 k까지 가는 거리를 넣어준다.
        result=[max_node] # result에는 최단거리가 가장 먼 헛간번호가 담기게 된다.
    elif max_distance==distance[k]: # k번째 헛간까지의 거리와 max_distance가 같다면
        result.append(k) # result에 넣어준다.

# 출력 : 숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간의 개수
print(max_node, max_distance, len(result))