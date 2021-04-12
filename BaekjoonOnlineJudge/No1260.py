import sys

# 정점의 개수 n, 간선의 개수 m, 정점의 번호 v
n, m, v = map(int, sys.stdin.readline().split())

matrix = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    point1, point2 = map(int, sys.stdin.readline().split())
    matrix[point1][point2] = 1
    matrix[point2][point1] = 1

# DFS(깊이 우선 탐색)

visited = [] # 방문했던 노드를 담을 list

def dfs(start, visited):
    visited += [start]
    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and (i not in visited):
            dfs(i, visited)
    return visited

# BFS(너비 우선 탐색)

def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for each in range(len(matrix[start])):
            if matrix[n][each] == 1 and (each not in visited):
                visited.append(each)
                queue.append(each)
    return visited

# 결과 출력

print(*dfs(v, []))
print(*bfs(v))