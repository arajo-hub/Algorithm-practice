import sys

# 색상환에 포함된 색의 개수(4부터)
n = int(sys.stdin.readline())

# 색상환에서 선택할 색의 개수
k = int(sys.stdin.readline())

# 어떤 인접한 두 색도 동시에 선택하지 않고 k개의 색을 고를 수 있는 경우의 수
# 원형으로 되어있다는 것에 주의!

# i번째색을 선택하면 i-1번째를 선택할 수 없으므로
# i-2개의 색 중에서 j-1개를 선택하는 경우와 같다.
# i번째색을 선택하지 않을 때는 i-1개 색 중에서 k개를 고르는 경우의 수와 같다.
# 점화식 : dp[i][j] = dp[i-1][j] + dp[i-2][j-1]

# n번째 색을 선택한다면 n-1번째와 1번째 색을 선택할 수 없다.
# 그러므로 n-3개의 색 중에서 j-1개를 고르는 경우의 수와 같다.
# n번째 색을 고르지 않는다면 1 ~ (n-1)까지의 색 중에서 j개를 고를 경우의 수와 같다.
# 점화식 : dp[i][j] = dp[i-3][j-1] + dp[i-1][j]

dp = [[0] * 1002 for _ in range(1002)]

mod = 1000000003

for i in range(n+1):
    dp[i][1] = i
    dp[i][0] = 1

for j in range(2, n+1):
    for h in range(2, k+1):
        if j == n:
            dp[j][h] = dp[j-3][h-1] + dp[j-1][h]
        else:
            dp[j][h] = dp[j-1][h] + dp[j-2][h-1]
        dp[j][h] %= mod
print(dp[n][h])