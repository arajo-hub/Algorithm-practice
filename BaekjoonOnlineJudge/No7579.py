import sys

n, m=map(int, sys.stdin.readline().split())

a=[0]+list(map(int, sys.stdin.readline().split())) # 메모리의 바이트 수
c=[0]+list(map(int, sys.stdin.readline().split())) # 비활성화했을 경우의 비용

dp=[[0 for _ in range(sum(c)+1)] for _ in range(n+1)]
result=sum(c) # 비용의 최댓값

for i in range(1, n+1):
    byte=a[i]
    cost=c[i]

    for j in range(1, sum(c)+1):
        if j<cost:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(byte+dp[i-1][j-cost], dp[i-1][j])
        if dp[i][j]>=m:
            result=min(result, j)

if m!=0:
    print(result)
else:
    print(0)