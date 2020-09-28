import sys

N=int(sys.stdin.readline())
t=[]
p=[]
dp=[0]*(N+1)
max_value=0

for _ in range(N):
    x, y=map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)

for i in range(N-1, -1, -1):
    time=t[i]+i # 상담에 걸리는 시간 + 퇴사까지 남은 기간
    if time<=N: # 상담이 기간 안에 끝난다면 현재까지의 최고 이익을 계산하여 dp에 넣어준다.
        dp[i]=max(p[i]+dp[time], max_value)
        max_value=dp[i]
    else: # 상담이 기간 안에 끝나지 않는다면
        dp[i]=max_value # 그 상담은 진행하지 않고 통과한다.

print(max_value)