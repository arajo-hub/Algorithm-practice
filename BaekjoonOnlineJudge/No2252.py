import sys
from collections import deque

# 학생의 수
N, M = map(int, sys.stdin.readline().split())

array = []
degree =[0 for i in range(32001)]
graph = [[] for i in range(32001)]
queue = deque()

for _ in range(M):
    # 학생 a가 학생 b의 앞에 서야 함!
    a, b = map(int, sys.stdin.readline().split())
    array.append([a, b])

for a, b in array:
    degree[b] += 1
    graph[a].append(b)

for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    for j in graph[student]:
        degree[j] -= 1
        if degree[j] == 0:
            queue.append(j)
    print(student, end = "")