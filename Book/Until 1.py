# import sys

# N, K=map(int, sys.stdin.readline().split())

# cnt=0

# while (N!=1):
#     if N%K!=0:
#         N-=1
#     else:
#         N/=K
#     cnt+=1

# print(cnt)

# 2020년 10월 16일 풀이

import sys

n, k=map(int, sys.stdin.readline().split())

cnt=0
while(n!=1):
    if n%k==0:
        n/=k
    else:
        n-=1
    cnt+=1

print(cnt)