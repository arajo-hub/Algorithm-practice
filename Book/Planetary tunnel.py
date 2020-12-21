def findParent(parent, x):
    if parent[x]!=x:
        parent[x]=findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a=findParent(parent, a)
    b=findParent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

import sys

n=int(sys.stdin.readline()) # 행성의 개수
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1, n+1):
    parent[i]=i

x=[]
y=[]
z=[]

for j in range(1, n+1):
    dx, dy, dz=map(int, sys.stdin.readline().split())
    x.append((dx, j))
    y.append((dy, j))
    z.append((dz, j))

x.sort()
y.sort()
z.sort()

for k in range(n-1):
    edges.append((x[k+1][0]-x[k][0], x[k][1], x[k+1][1]))
    edges.append((y[k+1][0]-y[k][0], y[k][1], y[k+1][1]))
    edges.append((z[k+1][0]-z[k][0], z[k][1], z[k+1][1]))

edges.sort()

for edge in edges:
    cost, a, b=edge
    if findParent(parent, a)!=findParent(parent, b):
        unionParent(parent, a, b)
        result+=cost

print(result)