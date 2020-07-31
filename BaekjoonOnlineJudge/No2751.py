import sys

N = int(input())
numList = []

for i in range(N):
    numList.append(int(sys.stdin.readline()))

for i in sorted(numList):
    print(i)