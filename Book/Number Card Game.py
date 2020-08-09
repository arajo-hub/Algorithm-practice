import sys

N, M=map(int, sys.stdin.readline().split())

card=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

maxs=0

for i in range(N):
    if min(card[i])>maxs:
        maxs=min(card[i])

print(maxs)