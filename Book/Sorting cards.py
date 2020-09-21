import heapq
import sys

N=int(sys.stdin.readline())

heap=[]
for i in range(N):
    data=int(sys.stdin.readline())
    heapq.heappush(heap, data)

result=0

while len(heap)!=1:
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)
    sum_value=one+two
    result+=sum_value
    heapq.heappush(heap, sum_value)

print(result)