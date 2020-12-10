# import sys

# N=int(sys.stdin.readline())

# soldiers=list(map(int, sys.stdin.readline().split()))
# soldiers.reverse()

# dp=[1]*N

# # 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
# for i in range(1, N): # soldiers에서 한 개의 수를 기준으로 잡고
#     for j in range(0, i): # 그 수의 전에 있는 수들을 하나씩 꺼내어 기준과 비교한다.
#         if soldiers[j]<soldiers[i]: # 기준보다 작다면
#             dp[i]=max(dp[i], dp[j]+1) # dp[i]와 dp[j]+1 중 큰 값을 dp[i]로 한다.
#         # 만약 기준보다 크다면 dp[i]는 1인 채로 그냥 지나간다.

# print(N-max(dp))
# # max(dp)는 가장 긴 증가하는 부분 수열의 길이.
# # 그러므로 총 병사 수에서 가장 긴 증가하는 부분 수열의 길이를 빼주면
# # 열외시켜야 할 최소 병사 수가 된다.

# 2020년 12월 10일 풀이

import sys

n=int(sys.stdin.readline())

soldiers=list(map(int, sys.stdin.readline().split()))
soldiers.reverse()

dp=[1]*n

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j]<soldiers[i]:
            dp[i]=max(dp[i], dp[j]+1)

print(n-max(dp))