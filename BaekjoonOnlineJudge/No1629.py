import sys

a, b, c=map(int, sys.stdin.readline().split())

# a를 b번 곱하게 되면 시간 초과가 된다.
# 이럴 때 제곱근을 이용하면 된다.
# a^(b//2)를 변수 하나에 저장해서 그 변수를 제곱하고,
# b가 짝수였다면 그대로지만,
# b가 홀수였다면 a를 한 번 더 곱해준다.
# 그리고 그 값을 c로 나눈 나머지를 반환한다.

def power(a, b):
    if b==1:
        return a%c
    else:
        temp=power(a, b//2)
        if b%2==0:
            return temp*temp%c
        else:
            return temp*temp*a%c

result=power(a, b)

print(result)