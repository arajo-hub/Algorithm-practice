# 플로이드 워셜 알고리즘

import sys

INF=int(1e9)

N, M=map(int, sys.stdin.readline().split()) # 회사의 개수 N과 경로의 개수 M을 입력한다.
citymap=[[INF]*(N+1) for _ in range(N+1)] # 정보를 저장할 citymap리스트를 만든다.

for a in range(1, N+1):
    for b in range(1, N+1):
        if a==b: # 한 회사에서 자기자신으로 가는 데 걸리는 시간은
            citymap[a][b]=0 # 0으로 초기화한다.

for _ in range(M): # 어떤 회사가 경로로 연결되어있는지 citymap에 1로 표시한다.
    frompoint, topoint=map(int, sys.stdin.readline().split())
    citymap[frompoint][topoint]=1
    citymap[topoint][frompoint]=1

X, K=map(int, sys.stdin.readline().split()) # 물건 판매를 위해 가야할 X와 소개팅을 위해 가야할 K 입력

for h in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            citymap[i][j]=min(citymap[i][j], citymap[i][h]+citymap[h][j])
            # i에서 j까지 가는 데 걸리는 시간은 1. i에서 j까지 가는 시간과 2. i에서 h에 갔다가 h에서 j로 가는 시간 중 짧은 시간으로 한다.

distance=citymap[1][K]+citymap[K][X] # 이 문제에서는 1에서 출발하여 K를 들렀다가 X로 가므로 1에서 K까지 가는 데 걸리는 시간에 K에서 X로 가는 데 걸리는 시간을 더한다.

if distance>=INF:
    print("-1")
else:
    print(distance)