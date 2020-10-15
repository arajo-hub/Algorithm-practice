# import sys

# N, M=map(int, sys.stdin.readline().split())

# card=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# maxs=0

# for i in range(N):
#     if min(card[i])>maxs:
#         maxs=min(card[i])

# print(maxs)

# 2020년 10월 15일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())
result=0
for i in range(n):
    cardset=list(map(int, sys.stdin.readline().split()))
    cardset_min=min(cardset)
    result=max(cardset_min, result)

print(result)