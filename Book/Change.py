# n=int(input()) # 거스름돈

# coins=[500, 100, 50, 10] # 거슬러줄 동전들

# count=0
# for i in coins:
#     count+=n//i # 동전으로 거슬러줄 수 있는 갯수를 count에 더하고
#     n%=i # n은 나머지 잔돈이 된다.

# print(count)

# 2020년 12월 27일 풀이

import sys

n=int(sys.stdin.readline()) # 거스름돈 얼마?

coins=[500, 100, 50, 10]

count=0
for i in coins:
    count+=n//i # 동전으로 거슬러줄 수 있는 갯수를 count에 더하고
    n%=i # n은 나머지 잔돈이 된다.

print(count)