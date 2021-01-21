# 1. 내 풀이 (파스칼의 삼각형 이용)

from itertools import combinations
import sys

n, k=map(int, sys.stdin.readline().split())

# 이 문제는 11050번 문제보다 더 넓은 범위의 이항계수를 구해야 한다.
# 파스칼의 삼각형과 DP를 이용하여 문제에 접근
# DP의 n-1번째 배열 중 k번째 있는 수를 10007로 나눈 나머지를 구하면 된다.

dp=[]

for i in range(n+1):
    for j in range(i+1):
        if j==0:
            dp.append([1])
            continue
        if j==i:
            dp[i].append(1)
            continue
        else:
            dp[i].append(dp[i-1][j-1]+dp[i-1][j])

print(dp[-1][k]%10007)

# 2. 팩토리얼을 이용한 다른 풀이
# # 이항계수 = nCk = n!/(k!(n-k!))

# from math import factorial
# import sys

# n, k = map(int, sys.stdin.readline().split())
# result = factorial(n) // (factorial(k)*factorial(n-k))
# print(result % 10007)

# 이 문제의 경우, 더 넓은 범위의 이항 계수를 동적 계획법으로 구하는 문제라고 설명되어 있다.
# 문제의 취지에 맞게 DP를 이용하여 푼다면 파스칼의 삼각형을 이용하는 방법(내 풀이)가 맞고,
# 좀 더 실행속도를 빠르게 하고 싶다면 팩토리얼을 이용하는 방법이 좋다.