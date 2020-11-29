# import sys

# N=int(sys.stdin.readline()) # 집의 수
# distance=list(map(int, sys.stdin.readline().split()))
# distance.sort()

# print(distance[(N-1)//2])

# 2020년 11월 30일 풀이

import sys

n=int(sys.stdin.readline())

house=list(map(int, sys.stdin.readline().split()))

house.sort()
print(house[(n-1)//2])