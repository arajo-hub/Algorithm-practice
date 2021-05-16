import sys

def bellmanFord():
    global isPossible

    for each in range(n):
        for i in range(1, n+1):
            for wei, vec in adjList[i]: # 한 도시에 연결된 노선을 탐색
                if dist[i] != INF and dist[vec] > dist[i] + wei: # 이미 방문했던 노선이고, 연결된 도시에 가는 비용이 현재 도시에서 가는 비용보다 비싸다면
                    dist[vec] = dist[i] + wei # 최소비용으로 바꿔주고
                    if each == n-1:
                        isPossible = False

# 도시의 개수, 버스 노선의 개수
n, m = map(int, sys.stdin.readline().split())

adjList = [[] for _ in range(n+1)]
INF = 2147483647
dist = [INF] * (n+1) # 거리는 아주 큰 값으로 초기화.
dist[1] = 0 # 시작은 0으로.
isPossible = True

for _ in range(m):
    # 도시 a에서 도시 b로 가는 비용 c
    a, b, c = map(int, sys.stdin.readline().split())
    adjList[a].append((c, b))

bellmanFord()

if not isPossible:
    print(-1)
else:
    for d in dist[2:]:
        print(d if d != INF else -1)