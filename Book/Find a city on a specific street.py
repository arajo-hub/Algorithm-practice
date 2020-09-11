from collections import deque
import sys

N, M, K, X=map(int, sys.stdin.readline().split())
# N은 도시의 개수, M은 도로의 개수, K는 최단거리, X는 출발 도시의 번호

cities=[[]*N for _ in range(N+1)]

for i in range(M):
    A, B=list(map(int, sys.stdin.readline().split()))
    cities[A].append(B)

distance=[-1]*(N+1)
distance[X]=0 # 출발 도시까지의 거리는 0으로 설정

# BFS(너비 우선 탐색)
q=deque([X])
while q:
    now=q.popleft() # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in cities[now]:
        if distance[next_node]==-1: # 아직 방문하지 않은 도시라면
            distance[next_node]=distance[now]+1 # 최단 거리 갱신
            q.append(next_node)

check=False
for i in range(1, N+1):
    if distance[i]==K:
        print(i)
        check=True

if check==-False:
    print(-1)