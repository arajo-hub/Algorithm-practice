import sys

answer=0

N=int(sys.stdin.readline())

times=list(map(int, sys.stdin.readline().split()))[:N+1]
times.sort()

for i in range(len(times)):
    answer+=times[i]*(N-i)
print(answer)