import sys

N=int(sys.stdin.readline())

warehouse=list(map(int, sys.stdin.readline().split()))

dp=[0]*100

dp[0]=warehouse[0]

dp[1]=max(warehouse[0], warehouse[1])

for i in range(2, N):
    dp[i]=max(dp[i-1], dp[i-2]+warehouse[i])

print(dp[N-1])