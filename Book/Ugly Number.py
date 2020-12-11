# import sys

# N=int(sys.stdin.readline())
# ugly=[0]*N # 못생긴 수들을 넣을 리스트
# ugly[0]=1 # 첫번째 못생긴 수는 1

# i2=i3=i5=0 # 2와 곱할 수, 3과 곱할 수, 5와 곱할 수를 가리키는 index
# next2, next3, next5=2, 3, 5

# for i in range(1, N):
#     ugly[i]=min(next2, next3, next5)
#     if ugly[i]==next2:
#         i2+=1
#         next2=ugly[i2]*2
#     if ugly[i]==next3:
#         i3+=1
#         next3=ugly[i3]*3
#     if ugly[i]==next5:
#         i5+=1
#         next5=ugly[i5]*5

# print(ugly[N-1])

# 2020년 12월 11일 풀이

import sys

n=int(sys.stdin.readline())

ugly=[0]*n
ugly[0]=1

multiply2=multiply3=multiply5=0
next2, next3, next5=2, 3, 5

for i in range(1, n):
    ugly[i]=min(next2, next3, next5)
    if ugly[i]==next2:
        multiply2+=1
        next2=ugly[multiply2]*2
    if ugly[i]==next3:
        multiply3+=1
        next3=ugly[multiply3]*3
    if ugly[i]==next5:
        multiply5+=1
        next5=ugly[multiply5]*5

print(ugly[n-1])