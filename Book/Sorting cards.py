# import heapq
# import sys

# N=int(sys.stdin.readline())

# heap=[]
# for i in range(N):
#     data=int(sys.stdin.readline())
#     heapq.heappush(heap, data)

# result=0

# while len(heap)!=1:
#     one=heapq.heappop(heap)
#     two=heapq.heappop(heap)
#     sum_value=one+two
#     result+=sum_value
#     heapq.heappush(heap, sum_value)

# print(result)

# 2020년 12월 2일 풀이

import heapq
import sys

n=int(sys.stdin.readline()) # 카드묶음 개수

heap=[]
for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

total=0

while len(heap)!=1:
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)
    sumVal=one+two
    total+=sumVal
    heapq.heappush(heap, sumVal)

print(total)