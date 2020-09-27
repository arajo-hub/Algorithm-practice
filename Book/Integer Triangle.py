import sys

N=int(sys.stdin.readline())
dp=[]

for _ in range(N):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(i+1):
        if j==0: # 왼쪽 위에서 내려오는 경우
            up_left=0
        else:
            up_left=dp[i-1][j-1]
        if j==i: # 바로 위에서 내려오는 경우
            up=0
        else:
            up=dp[i-1][j]
        dp[i][j]=dp[i][j]+max(up_left, up)

print(max(dp[N-1]))