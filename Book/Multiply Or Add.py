# import sys

# S=sys.stdin.readline().strip('\n')

# result=0
# for num in S:
#     if int(num)<=1 or result<=1:
#         result+=int(num)
#     else:
#         result*=int(num)

# print(result)

# 2020년 11월 9일 풀이

import sys

s=sys.stdin.readline().strip('\n')

result=0

for num in s:
    if int(num)<=1 or result<=1:
        result+=int(num)
    else:
        result*=int(num)

print(result)