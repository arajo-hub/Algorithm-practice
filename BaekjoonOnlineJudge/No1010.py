import sys
from math import factorial

t=int(sys.stdin.readline())

for tc in range(t):
    n, m=map(int, sys.stdin.readline().split())
    print((factorial(m)//(factorial(n)*factorial(m-n))))