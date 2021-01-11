# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

import sys

S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()

len1 = len(S1)
len2 = len(S2)

matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if S1[i-1] == S2[j-1]: # S1과 S2에 가장 최근에 추가된 글자가 서로 같다면
            matrix[i][j] = matrix[i-1][j-1] + 1 # 길이는 이전의 가장 긴 길이에 +1이 된다.
        else: # 추가된 글자가 서로 다르다면
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1]) # 기존에 주어진 문자열로 만들 수 있었던 최대 길이를 갖게 된다.

print(matrix[-1][-1])