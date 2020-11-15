# import sys

# N=list(map(int, sys.stdin.readline().strip('\n')))

# if sum(N[:len(N)//2])==sum(N[len(N)//2:]):
#     print("LUCKY")
# else:
#     print("READY")

# 2020년 11월 15일 풀이

import sys

n=list(map(int, sys.stdin.readline().strip('\n')))

left=n[:len(n)//2]
right=n[len(n)//2:]

if sum(left)==sum(right):
    print("LUCKY")
else:
    print("READY")