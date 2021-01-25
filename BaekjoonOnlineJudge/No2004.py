import sys

def divideFive(n):
    result=0
    while (n!=0):
        n//=5
        result+=n
    return result

def divideTwo(n):
    result=0
    while (n!=0):
        n//=2
        result+=n
    return result

n, m=map(int, sys.stdin.readline().split())

print(min(divideTwo(n)-divideTwo(m)-divideTwo(n-m), divideFive(n)-divideFive(m)-divideFive(n-m)))