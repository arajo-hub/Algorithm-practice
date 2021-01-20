# 이항계수

from itertools import combinations
import sys

n, k=map(int, sys.stdin.readline().split())

combi=combinations(range(n), k)

result=0
for c in combi:
    result+=1

print(result)