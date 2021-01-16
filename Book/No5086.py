import sys

while (True):
    x, y=map(int, sys.stdin.readline().split())
    if x==0 and y==0:
        break
    if x<y and y%x==0: # x가 y의 약수
        print("factor")
    elif x>y and x%y==0: # x가 y의 배수라면
        print("multiple")
    else:
        print("neither")