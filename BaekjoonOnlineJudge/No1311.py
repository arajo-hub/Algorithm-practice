import sys

INF = float('inf')

n = int(sys.stdin.readline())

d = []

for _ in range(n):
    d.append(list(map(int, sys.stdin.readline().split())))
dp = [[-1] * (1 << n) for _ in range(20)]
    
def dfs(x, visited):
    if visited == (1 << n) - 1:
        return 0
    if dp[x][visited] != -1:
        return dp[x][visited]
    dp[x][visited] = INF
    for i in range(n):
        if visited & (1 << i):
            continue
        dp[x][visited] = min(dp[x][visited], dfs(x + 1, visited | (1 << i)) + d[x][i])
    return dp[x][visited]
    
print(dfs(0, 0))