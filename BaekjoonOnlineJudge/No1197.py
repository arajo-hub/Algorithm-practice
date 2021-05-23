# 최소 스패닝 트리
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리

import sys

def find(x):
    if x == root[x]:
        return x
    else:
        y = find(root[x])
        root[x] = y
        return y

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        root[root_y] = root_x

# 정점의 개수, 간선의 개수
v, e = map(int, sys.stdin.readline().split())

g = []

root = [i for i in range(v+1)]

for _ in range(e):
    # a번 정점과 b번 정점이 가중치 c인 간선으로 연결되어 있다는 의미
    a, b, c = map(int, sys.stdin.readline().split())
    g.append([c, a, b])

g.sort(key = lambda x:x[0])

connected = 0 # 모두 연결되었는지 체크
MST = 0 # 최소 스패닝 트리의 가중치

for j in range(e):
    distance = g[j][0]
    start = g[j][1]
    end = g[j][2]

    if find(start) != find(end):
        union(start, end)
        MST += distance
        connected += 1
    if connected == v-1:
        break

print(MST)