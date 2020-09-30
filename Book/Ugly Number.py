import sys

N=int(sys.stdin.readline())
ugly=[0]*N # 못생긴 수들을 넣을 리스트
ugly[0]=1 # 첫번째 못생긴 수는 1

i2=i3=i5=0 # 2와 곱할 수, 3과 곱할 수, 5와 곱할 수를 가리키는 index
next2, next3, next5=2, 3, 5

for i in range(1, N):
    ugly[i]=min(next2, next3, next5)
    if ugly[i]==next2:
        i2+=1
        next2=ugly[i2]*2
    if ugly[i]==next3:
        i3+=1
        next3=ugly[i3]*3
    if ugly[i]==next5:
        i5+=1
        next5=ugly[i5]*5

print(ugly[N-1])