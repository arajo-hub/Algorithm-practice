import heapq
import sys

n, m=map(int, sys.stdin.readline().split())
INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
start=1 # 첫번째 헛간에서 시작

for i in range(m):
    a, b=map(int, sys.stdin.readline().split())
    graph[a].append((b, 1)) # a번 헛간과 연결된 헛간번호와 이동비용을 graph의 a번째 칸에 추가해준다.
    graph[b].append((a, 1)) # b번 헛간에도 연결된 헛간번호와 이동비용을 graph의 b번째 칸에 추가해준다.

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start)) # q에 (최단거리(=최소이동비용), 현재위치) 이런 식으로 추가
    distance[start]=0
    while q:
        dist, now=heapq.heappop(q)
        if distance[now]<dist: # 현재위치의 거리가 최단거리보다 작다면 continue
            continue
        for j in graph[now]: # 현재위치에서 갈 수 있는 (헛간번호, 이동비용)(=j)을 꺼내서
            cost=dist+j[1] # 이동비용에 그 이동비용을 추가해주고
            if cost<distance[j[0]]: # 만약 그렇게 바뀐 새 이동비용이 새 헛간(j[0])까지의 이동비용보다 작다면
                distance[j[0]]=cost # 더 작은 값으로 바꿔준다.
                heapq.heappush(q, (cost, j[0])) # 그리고 q에 바뀐 값들을 추가해준다.

dijkstra(start)

max_node=0
max_distance=0
result=[]

for k in range(1, n+1):
    if max_distance<distance[k]: # k번째 헛간까지 가는 거리가 max_distance보다 크다면
        max_node=k # 최단거리가 가장 먼 헛간번호를 k로 넣어준다.
        max_distance=distance[k] # 그리고 max_distance에 k까지 가는 거리를 넣어준다.
        result=[max_node] # result에는 최단거리가 가장 먼 헛간번호가 담기게 된다.
    elif max_distance==distance[k]: # k번째 헛간까지의 거리와 max_distance가 같다면
        result.append(k) # result에 넣어준다.

print(max_node, max_distance, len(result))