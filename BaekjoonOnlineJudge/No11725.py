import sys

node = int(sys.stdin.readline()) # 노드의 개수
graph = [[] for _ in range(node + 1)]
parent = [[] for _ in range(node + 1)]

# 트리를 그래프 형태로 생성

for _ in range(node - 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph_list, start, parent):
    
    stack = [start]

    while stack:
        node = stack.pop() # 시작점을 뽑는다.
        for i in graph_list[node]: # 시작점의 node를 하나씩 꺼낸다.
            parent[i].append(node) # 그 각각 node에 시작점을 넣어준다.
            stack.append(i) # 그리고 stack에 쌓아서 다음 시작점이 되도록 한다.
            graph_list[i].remove(node) # 작업이 끝난 node는 뽑는다.
    
    return parent

for i in list(dfs(graph, 1, parent))[2:]:
    print(i[0])