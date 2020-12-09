# import sys

# N=int(sys.stdin.readline())
# t=[]
# p=[]
# dp=[0]*(N+1)
# max_value=0

# for _ in range(N):
#     x, y=map(int, sys.stdin.readline().split())
#     t.append(x)
#     p.append(y)

# for i in range(N-1, -1, -1):
#     time=t[i]+i # 상담에 걸리는 시간 + 퇴사까지 남은 기간
#     if time<=N: # 상담이 기간 안에 끝난다면 현재까지의 최고 이익을 계산하여 dp에 넣어준다.
#         dp[i]=max(p[i]+dp[time], max_value)
#         max_value=dp[i]
#     else: # 상담이 기간 안에 끝나지 않는다면
#         dp[i]=max_value # 그 상담은 진행하지 않고 통과한다.

# print(max_value)

# 2020년 12월 9일 풀이

import sys

n=int(sys.stdin.readline()) # 퇴사까지 남은 일수

time=[]
pay=[]
dp=[0]*(n+1)
maxValue=0

for i in range(n):
    t, p=map(int, sys.stdin.readline().split()) # 상담에 소요되는 시간 t, 이익 p
    time.append(t)
    pay.append(p)

for j in range(n-1, -1, -1): # 뒤에서부터 탐색해온다.
    allTime=time[j]+j # j일부터 시작하는 상담이 진행되는 그 시간과 j일을 더한다.
    if allTime<=n: # 위에서 더한 'j+상담진행시간'(=allTime)이 n일보다 작다면(=예정보다 일찍 끝나거나 예정대로 걸린다면)
        dp[j]=max(pay[j]+dp[allTime], maxValue)
        # 상담을 진행했을 때의 이익에 상담을 진행해서 받은 이익을 더한 값(pay[j]+dp[allTime])과
        # 현재까지의 최고이익 중 큰 값을 dp에 넣는다.
        maxValue=dp[j] # 그리고 최고이익에 현재까지의 최고이익을 넣는다.
    else: # 상담이 예정기간을 넘어 진행할 수 없다면,
        dp[j]=maxValue # dp에 최고이익을 넣는다.

print(maxValue)