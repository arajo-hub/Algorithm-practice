# 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 구하는 문제
# 루트가 있는 트리를 가중치가 있는 간선들로 준다는 조건

from collections import deque
import sys

def bfs(x, mode):

    q = deque()
    
    q.append(x)
    
    c = [-1 for _ in range(n)]
    
    c[x] = 0
    
    while q:
        x = q.popleft()
        for w, nx in matrix[x]:
            if c[nx] == -1:
                c[nx] = c[x] + w
                q.append(nx)

    if mode == 1:
        return c.index(max(c))
    else:
        return max(c)

n = int(sys.stdin.readline())
matrix = [[] for _ in range(n)]

for i in range(n-1):
    # 순서대로 부모 노드의 번호, 자식 노드의 번호, 간선의 가중치
    x, y, w = map(int, sys.stdin.readline().split())
    # 연결된 노드와 그 가중치를 표시
    matrix[x-1].append([w, y-1])
    matrix[y-1].append([w, x-1])

print(bfs(bfs(0, 1), 2))