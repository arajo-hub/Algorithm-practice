import sys

n=int(sys.stdin.readline()) # 링의 개수

r=list(map(int, sys.stdin.readline().split())) # 각 링의 반지름들

# 첫번째 링을 제외한 각각의 링에 대해서 첫번째 링을 한 바퀴 돌리면 그 링은 몇 바퀴 도는지 기약 분수 형태 A/B로 출력

# 1. 내 풀이
# for i in range(1, n):
#     num1, num2 = r[0], r[i]
#     while num2 != 0:
#         num1 = num1 % num2
#         num1, num2 = num2, num1

#     print(r[0]//num1, "/", r[i]//num1, sep = '')

# 2. 파이썬에서 지원하는 gcd(최대공약수) 이용

from math import gcd
# def gcd(a: int, b: int)
# greatest common divisor of x and y

gcds=[gcd(r[0], r[i]) for i in range(1, n)]

for i in range(1, n):
    print(r[0]//gcds[i-1], "/", r[i]//gcds[i-1], sep="")