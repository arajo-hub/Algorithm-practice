import sys

n = int(sys.stdin.readline()) # 행렬의 개수

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        x = j + i
        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + matrix[j][0]*matrix[k][1]*matrix[x][1])

print(dp[0][n-1])
