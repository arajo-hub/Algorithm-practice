import sys

INF=int(1e9)

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())

graph=[[INF]*(N+1) for _ in range(N+1)]

for a in range(1, N+1):
    for b in range(1, N+1):
        if a==b:
            graph[a][b]=0 # 도시의 출발지와 목적지가 같은 경우는 0

for _ in range(M):
    a, b, c=map(int, input().split())
    if c<graph[a][b]:
        graph[a][b]=c # 버스의 정보 입력(a도시에서 b도시까지 가는 데 필요한 비용 c)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
            # a부터 k까지 갔다가 k에서 b로 가는 비용과
            # a에서 b로 가는 비용 중 적은 비용을 저장한다.

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b]==INF: # 갈 수 없는 경우는 0 출력
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()