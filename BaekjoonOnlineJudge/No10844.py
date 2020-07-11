n = int(input())
dp = [[0 for i in range(10)] for j in range(101)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n]) % 1000000000)

# 코드의 출처는 https://pacific-ocean.tistory.com/151
# 각 자리수에서 맨 뒤에 올 수 있는 숫자의 갯수를 정리해보면
# 1일 때, 0 1 1 1 1 1 1 1 1 1
# 2일 때, 1 1 2 2 2 2 2 2 2 1
# 3일 때, 1 3 3 4 4 4 4 4 3 2
# 가 된다.
# 이를 살펴보면, 양 대각선에 있는 값을 더한 값으로 계속 나아감을 알 수 있다.