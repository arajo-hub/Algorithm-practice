import sys

N=int(sys.stdin.readline())

temp1, temp2, temp3=1, 2, 0

if N<=2:
    print(N)
else:
    for i in range(0, N-2):
        temp3=temp1+temp2
        temp1=temp2%15746
        temp2=temp3%15746
    print(temp3%15746)

# 이 문제는 어려운 것 같아보이지만 사실 피보나치수열의 문제이다.