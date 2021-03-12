import sys
input=sys.stdin.readline
INF=sys.maxsize
def dist(a,b):
    return (a[0]-b[0])**2+(a[1]-b[1])**2

def divide(start,end):
    if start==end:
        return INF
    elif end-start==1:
        return dist(arr[end],arr[start])
    mid=(start+end)//2
    temp=min(divide(start,mid),divide(mid,end))

    candicate=[]
    for i in range(start,end+1):
        if (arr[mid][0]-arr[i][0])**2<temp:
            candicate.append(arr[i])
    candicate.sort(key=lambda x:x[1])
    lc=len(candicate)
    for i in range(lc-1):
        for j in range(i+1,lc):
            dy=(candicate[i][1]-candicate[j][1])**2
            if dy<temp:
                temp=min(temp,dist(candicate[i],candicate[j]))
            else:
                break
    return temp

n=int(input())
arr=[]
for i in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort()

print(divide(0,len(arr)-1))