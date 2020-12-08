# import sys

# N=int(sys.stdin.readline())
# dp=[]

# for _ in range(N):
#     dp.append(list(map(int, sys.stdin.readline().split())))

# for i in range(1, N):
#     for j in range(i+1):
#         if j==0: # 왼쪽 위에서 내려오는 경우
#             up_left=0
#         else:
#             up_left=dp[i-1][j-1]
#         if j==i: # 바로 위에서 내려오는 경우
#             up=0
#         else:
#             up=dp[i-1][j]
#         dp[i][j]=dp[i][j]+max(up_left, up)

# print(max(dp[N-1]))

# 2020년 12월 8일 풀이

import sys

n=int(sys.stdin.readline())
dp=[]

for _ in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))
print(dp)
for i in range(1, n):
    for j in range(i+1):
        if j==0: # 왼쪽 위가 존재하지 않는 경우는 0
            upLeft=0
        else: # 왼쪽 위가 존재하는 경우는 왼쪽 위의 값을 가져오고
            upLeft=dp[i-1][j-1]
        if j==i: # 위에 숫자가 존재하지 않는 경우는 0
            up=0
        else: # 위에 숫자가 존재하는 경우는 위에 있는 값을 가져오고
            up=dp[i-1][j]
        dp[i][j]=dp[i][j]+max(upLeft, up)

print(max(dp[n-1]))