# import sys

# N=int(sys.stdin.readline())

# cnt=0
# for hour in range(N+1):
#     for minute in range(60):
#         for second in range(60):
#             if '3' in str(hour)+str(minute)+str(second):
#                 cnt+=1

# print(cnt)

# 2020년 10월 18일 풀이

import sys

n=int(sys.stdin.readline())
cnt=0
for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            if '3' in str(h)+str(m)+str(s):
                cnt+=1

print(cnt)