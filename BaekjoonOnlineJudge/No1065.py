N=int(input())
cnt=99

if N<100:
    cnt=N
else:
    for j in range(100, N+1):
        j=str(j)
        if int(j[0])-int(j[1])==int(j[1])-int(j[2]):
            cnt+=1
print(cnt)

# 위 코드는 메모리 29380KB, 시간 64ms, 코드길이 178B.
# 다섯달 전에 푼 아래 코드는 메모리 29284KB, 시간 52ms, 코드길이 352B.

import sys

num=sys.stdin.readline()
numlist=list(num)
resultset=[]
count=0

for j in range(1, int(num)+1):
    if j<100:
        count=j
    else:
        j=list(str(j))
        for i in range(1, len(j)):
            resultset.append(int(j[-(i+1)])-int(j[-i]))
        if len(set(resultset))==1:
            count+=1
        resultset=[]

print(count)