from heapq import heappush, heappop
import sys

INF = 100000000

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])
    dp = [INF for i in range(n+1)]
    dp[start] = 0
    while heap:
        we, nu = heappop(heap)
        for ne, nw in matrix[nu]:
            wei = we + nw
            if dp[ne] > wei:
                dp[ne] = wei
                heappush(heap, [wei, ne])
    return dp

# 테스트케이스
tc = int(sys.stdin.readline())

for i in range(tc):
    
    # 교차로 n, 도로 m, 목적지 t
    n, m, t = map(int, sys.stdin.readline().split())
    
    # 예술가들의 출발지 s, 예술가들이 지나간 g와 h 교차로 사이의 도로
    s, g, h = map(int, sys.stdin.readline().split())

    matrix = [[] for _ in range(n+1)]

    de = []
    
    for j in range(m):
        # a, b 사이에 길이 d의 양방향 도로가 있다.
        a, b, d = map(int, sys.stdin.readline().split())
        matrix[a].append([b, d])
        matrix[b].append([a, d])

    for k in range(t):
        # t개의 목적지 후보
        de.append(int(sys.stdin.readline()))
    
    s_dijkstra = dijkstra(s) # s에서 시작할 때
    g_dijkstra = dijkstra(g) # g에서 시작할 때
    h_dijkstra = dijkstra(h) # h에서 시작할 때

    answer = []

    for i in de: # 후보들 하나씩 꺼내서 탐색

        # s -> g -> h -> 도착지점이 s -> 도착지점으로 가는 비용과 같거나
        # s -> h -> g -> 도착지점이 s -> 도착지점으로 가는 비용과 같을 때
        if s_dijkstra[g] + g_dijkstra[h] + h_dijkstra[i] == s_dijkstra[i] or s_dijkstra[h] + h_dijkstra[g] + g_dijkstra[i] == s_dijkstra[i]:
            answer.append(i)
    
    answer.sort()
    
    for each in answer:
        print(each, end = ' ')
    print()