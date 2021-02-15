import heapq
import sys

n=int(sys.stdin.readline()) # 외치는 정수의 개수

left, right=[], []

for _ in range(n):
    num=int(sys.stdin.readline())
    if len(left)==len(right):
        heapq.heappush(left, (-num, num))
        print(left)
        print(right)
    else:
        heapq.heappush(right, (num, num))
        print(left)
        print(right)
    
    if right and left[0][1]>right[0][1]:
        left_value=heapq.heappop(left)[1]
        right_value=heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
        print(left)
        print(right)
    
    print(left[0][1])

# https://inspirit941.tistory.com/200