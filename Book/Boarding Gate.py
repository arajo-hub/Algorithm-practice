def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

import sys

G=int(sys.stdin.readline())
P=int(sys.stdin.readline())

parent=[0]*(G+1)

for i in range(1, G+1):
    parent[i]=i # 부모를 자기 자신으로 초기화

result=0
for _ in range(P):
    data=find_parent(parent, int(sys.stdin.readline()))
    if data==0:
        break
    union_parent(parent, data, data-1) # 루트노드가 0이 아니라면 왼쪽의 집합과 합치기
    result+=1

print(result)