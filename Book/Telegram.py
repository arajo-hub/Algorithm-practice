# 다익스트라 알고리즘 풀이

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, start = map(int, input().split()) # 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C를 입력한다.
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M): # 경로가 어떻게 연결되어있는지 정보를 입력한다.
    x, y, z = map(int, input().split()) # 도시(x)와 도시(y) 그리고 가는 데 걸리는 시간(z)
    graph[x].append((y, z)) # [x, (y, z)]의 형태로 저장된다.

def dijkstra(start):
   q = []
   heapq.heappush(q, (0, start)) # q에 (0, start)를 추가한다. (거리, 도시)
   distance[start] = 0 # 시작점의 최단거리는 0
   while q:
        dist, now = heapq.heappop(q) # dist는 거리, now는 현재 있는 도시
        if distance[now] < dist: # 현재 있는 도시까지의 최단경로(dist)보다 현재 도시까지의 경로(distance[now])가 작다면 반복문으로 돌아간다.
            continue
        for i in graph[now]: # 참고로 graph에는 같은 x일 경우, [도시x, (도시y, 거리z), (또 다른 도시y, 또 다른 거리z)]의 형태로 저장되어 있다.
            cost = dist + i[1] # i[1]은 위의 graph에서 (y, z) 중 거리 z를 말한다.
            if cost < distance[i[0]]: # 거리를 더한 값(cost)가 distance[i[0]](도시 y까지의 거리)보다 작다면
                distance[i[0]] = cost # 도시 y까지의 거리를 cost로 바꿔주고
                heapq.heappush(q, (cost, i[0])) # q에 cost와 현재 도시 를 넣어준다.

dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != 1e9:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)