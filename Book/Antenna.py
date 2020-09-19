import sys

N=int(sys.stdin.readline()) # 집의 수
distance=list(map(int, sys.stdin.readline().split()))
distance.sort()

print(distance[(N-1)//2])