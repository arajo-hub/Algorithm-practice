# import sys

# S=sys.stdin.readline().strip('\n')
# result=0

# count0, count1=0, 0

# if S[0]=='1':
#     count0+=1
# else:
#     count1+=1

# for i in range(len(S)-1):
#     if S[i]!=S[i+1]:
#         if S[i+1]=='1':
#             count0+=1
#         else:
#             count1+=1

# print(min(count0, count1))

# 2020년 11월 10일 풀이

import sys

s=sys.stdin.readline().strip('\n')
countZero=0
countOne=0

if s[0]=='1':
    countOne+=1
else:
    countZero+=1

for j in range(len(s)-1):
    if s[j]!=s[j+1]: # 연속된 두 수가 서로 다른 값일 때
        if s[j+1]=='1': # 나중의 수가 1이라면
            countZero+=1 # 현재의 수는 0이므로 countZero를 1 올려준다.
        else: # 나중의 수가 0이라면
            countOne+=1 # 현재의 수는 1이므로 countOne을 1 올려준다.

print(min(countZero, countOne))