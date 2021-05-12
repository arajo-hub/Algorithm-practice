# 팰린드롬(palindrome)
# 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어

import sys

# 수열의 크기
n = int(sys.stdin.readline())

dp = [[0] * n for i in range(n)]

# 수열 만들기
num_list = list(map(int, sys.stdin.readline().split()))

for j in range(n):
    for start in range(n):
        end = start + j
        if end >= n:
            break
        if start == end:
            dp[start][end] = 1
            continue
        if start + 1 == end:
            if num_list[start] == num_list[end]:
                dp[start][end] = 1
            continue
        if num_list[start] == num_list[end] and dp[start + 1][end - 1]:
            dp[start][end] = 1

# 질문의 개수
m = int(sys.stdin.readline())

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s - 1][e - 1])