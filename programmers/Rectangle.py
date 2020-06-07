import math

def solution(w,h):
    return w*h-(w+h-math.gcd(w,h))

# gcd는 최대공약수를 구하는 함수이다.