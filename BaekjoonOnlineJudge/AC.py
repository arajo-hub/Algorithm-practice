import sys
from collections import deque

for i in range(int(sys.stdin.readline())):
    p=sys.stdin.readline().strip('\n')
    n=int(sys.stdin.readline())
    pList=sys.stdin.readline().strip('\n')
    if n==0:
        pList=[]
    else:
        pList=deque(''.join(pList[1:-1]).split(','))
    cnt=0
    tf=True
    for i in p:
        if i=='R':
            cnt+=1
        elif i=='D':
            if not pList:
                tf=False
                break
            if cnt%2==0:
                pList.popleft()
            else:
                pList.pop()
    if not tf:
        print("error")
    else:
        if cnt%2==0:
            print("[", end="")
            print(",".join(pList), end="")
            print("]")
        else:
            pList.reverse()
            print("[", end="")
            print(",".join(pList), end="")
            print("]")