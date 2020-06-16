import sys

N=int(sys.stdin.readline())
numList=[]

for i in range(N):
    if i==0:
        if len(numList)==0:
            print(0)
        numList.pop(max(numList))
    else:
        numList.append(i)