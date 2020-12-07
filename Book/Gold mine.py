# import sys

# for tc in range(int(sys.stdin.readline())):
#     n, m=map(int, sys.stdin.readline().split()) # 금광 입력
#     array=list(map(int, sys.stdin.readline().split())) # 금광의 금 정보 입력

#     dp=[]
#     index=0
#     for i in range(n):
#         dp.append(array[index:index+m]) # 한 줄로 입력받은 금 정보를 맵으로 dp에 저장
#         index+=m

#     # 다이나믹 프로그래밍 수행
#     # 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다는 조건이 있으므로
#     # 왼쪽 위에서 오는 경우, 왼쪽 아래에서 오는 경우, 왼쪽에서 오는 경우 3가지가 있다.
#     for j in range(1, m):
#         for i in range(n):
#             if i==0: # 왼쪽 위에서 오는 경우
#                 left_up=0
#             else:
#                 left_up=dp[i-1][j-1]
#             if i==n-1: # 왼쪽 아래에서 오는 경우
#                 left_down=0
#             else:
#                 left_down=dp[i+1][j-1]
#             # 왼쪽에서 오는 경우
#             left=dp[i][j-1]
#             dp[i][j]=dp[i][j]+max(left_up, left_down, left)

#     result=0
#     for i in range(n):
#         result=max(result, dp[i][m-1])

#     print(result)

# 2020년 12월 7일 풀이

import sys

for tc in range(int(sys.stdin.readline())):
    n, m=map(int, sys.stdin.readline().split()) # 금광의 크기(가로 n * 세로 m)
    gold=list(map(int, sys.stdin.readline().split())) # 금 정보가 들어있는 배열

    dp=[]
    index=0
    for i in range(n):
        dp.append(gold[index:index+m]) # 한 줄로 받은 금 정보를 나눠서 맵형식으로 저장
        index+=m
    
    for j in range(1, m):
        for k in range(n):
            if k==0:
                leftUp=0
            else:
                leftUp=dp[k-1][j-1]
            if k==(n-1):
                leftDown=0
            else:
                leftDown=dp[k+1][j-1]
            left=dp[k][j-1]
            dp[k][j]=dp[k][j]+max(leftUp, leftDown, left)
    
    result=0
    for i in range(n):
        result=max(result, dp[i][m-1])

    print(result)