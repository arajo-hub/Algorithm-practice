import sys

N=int(sys.stdin.readline())

dp=[0]*1001

dp[1]=1
dp[2]=3

# 주어진 덮개는 [1, 2], [2, 1], [2, 2]이다.

# 넓이가 [1, 2]라면(N=1), [1, 2] 덮개로만 채울 수 있으므로 경우의 수는 1.

# 넓이가 [2, 2]라면(N=2), 각각의 덮개로 채울 수 있으므로 세 가지 경우.

# 넓이가 [3, 2]라면(N=3),
# 1. [2, 2]로 채우는 경우, 나머지 [1, 2]는 [1, 2]덮개로 채우는 1가지 경우만 존재.
# 2. [1, 2]로 채우는 경우, [1, 2]로 채우고 나머지를 [2, 1]로 채우거나, 나머지를 [2, 2]로 채우는 2가지 경우가 존재.
# 즉, N=(i-2)일 때는 항상 두 가지 경우가 존재하므로 dp[i-2]에 2를 곱해준다.
# 그 결과, 경우의 수는 5가지가 된다.

# 넓이가 [4, 2]라면(N=4),
# [3, 2]로 채우는 경우는 5가지(나머지 [1, 2]는 [1, 2] 덮개로 채운다.)
# [2, 2]로 채우고 [2, 1]로 채우는 경우는 3가지
# [2, 2]로 채우고 [2, 2]로 채우는 경우는 3가지
# 그 결과, 경우의 수는 11가지가 된다.

for i in range(3, N+1):
    dp[i]=(dp[i-1]+2*dp[i-2])%796796

print(dp[N])