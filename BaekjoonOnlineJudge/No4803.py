import sys

k=1
def dfs(x,start):
    visit[x]=1

    for i in arr[x]:
        if i==start:
            continue
        if visit[i]==1:
            return False
        if dfs(i,x)==False:
            return False

    return True

while True:
    n,m=map(int, sys.stdin.readline().split())

    if n==0 and m==0:
        break

    arr=[[] for i in range(n+1)]
    visit=[0]*(n+1)

    for i in range(m):
        a,b=map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    t=0
    for i in range(1,n+1):
        if visit[i]==0:
            if dfs(i,0)==True:
                t+=1

    if t > 1:
        print("Case", k, end="")
        print(":", end=" ")
        print("A forest of", t, end=" ")
        print("trees.")
    elif t == 0:
        print("Case", k, end="")
        print(":", end=" ")
        print("No trees.")
    elif t == 1:
        print("Case", k, end="")
        print(":", end=" ")
        print("There is one tree.")

    k += 1