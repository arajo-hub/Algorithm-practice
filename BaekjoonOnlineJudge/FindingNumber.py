import sys

N=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))
numdict={}
for i in A:
    numdict[i]=1

M=int(sys.stdin.readline())
testA=list(map(int, sys.stdin.readline().split()))

for j in testA:
    if j in numdict:
        print('1')
    else:
        print('0')