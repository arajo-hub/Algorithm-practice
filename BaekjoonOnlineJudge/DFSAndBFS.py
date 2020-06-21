N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1 # 무향그래프이기 때문에 대칭되는 위치의 값이 같다.

def dfs(current_node, row, foot_prints): # dfs(탐색을 시작할 정점의 번호, 정점들이 간선으로 연결된 트리(인접행렬), 지나간 정점을 저장할 비어있는 리스트)
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)
    return foot_prints


def bfs(start):
    queue = [start]
    foot_prints = [start]
    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]
    return foot_prints


print(*dfs(V, matrix, []))
print(*bfs(V))