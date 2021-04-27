def bfs(start):

    visited[start] = 1

    q = deque()
    q.append(start)

    while q:
        x = q.popleft()

        for i in matrix[x]:
            if visited[i]==0:
                visited[i]=-visited[x]
                q.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True

from collections import deque
import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    v, e = map(int, sys.stdin.readline().split())

    isTrue = True

    matrix = [[] for i in range(v+1)]
    visited = [0 for i in range(v+1)]

    for _ in range(e):
        point1, point2 = map(int, sys.stdin.readline().split())
        matrix[point1].append(point2)
        matrix[point1].append(point2)

    for i in range(1, v+1):
        if visited[i] == 0:
            if not bfs(i):
                isTrue = False
                break
    
    if isTrue:
        print("YES")
    else:
        print("NO")