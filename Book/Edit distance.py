def edit_dist(str1, str2):
    n=len(str1)
    m=len(str2)

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    # 세로는 변경전 문자열, 가로는 변경후 문자열
    # dp의 대각선을 따라서 몇 번 바꾸어야 하는지 표시된다.
    dp=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dp[i][0]=i

    for j in range(1, m+1):
        dp[0][j]=j # 바뀔 글자수만큼 [0]에 표시

    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1]==str2[j-1]: # 문자가 같다면
                dp[i][j]=dp[i-1][j-1] # 변화없이 그대로
            else: # 문자가 다르다면 왼쪽값, 위쪽값, 대각선값 중 가장 작은 값에 +1을 해준다.
                dp[i][j]=1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[n][m]

str1=input()
str2=input()

print(edit_dist(str1, str2))