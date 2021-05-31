import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

array = [[] for i in range(N+1)]
degree =[0 for i in range(N+1)]
heap = []
result = []

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    array[A].append(B)
    degree[B] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    q_number = heapq.heappop(heap)
    result.append(q_number)
    for j in array[q_number]:
        degree[j] -= 1
        if degree[j] == 0:
            heapq.heappush(heap, j)

for k in result:
    print(k, end = " ")