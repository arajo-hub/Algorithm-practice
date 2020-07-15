n = int(input()) # 계단 갯수를 입력받는다.
score = [0 for i in range(301)] # 0이 301개 들어있는 리스트를 만든다.
dp = [0 for i in range(301)] # 0이 301개 들어있는 dp를 만든다.

for i in range(n): # 계단별로
    score[i] = int(input()) # 점수를 입력한다.

print(score)

dp[0] = score[0] # 어차피 첫번째 계단은 밟아야 하므로 dp[0]에 score[0]을 저장한다.
dp[1] = score[0] + score[1] # dp[1]에는 score[0]하고 score[1]을 더한다.
dp[2] = max(score[1] + score[2], score[0] + score[2]) # dp[2]에는 dp[2]에 오는 경우의 수 중에 가장 높은 점수를 저장한다.

for i in range(3, n): # dp[2]까지는 위에서 채워놨으므로 dp[3]부터 dp를 채워간다.
    dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])

print(dp[n - 1])