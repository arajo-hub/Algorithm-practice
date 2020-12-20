# def find_parent(parent, x):
#     if parent[x]!=x:
#         parent[x]=find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a=find_parent(parent, a)
#     b=find_parent(parent, b)
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b

# import sys

# n, m=map(int, sys.stdin.readline().split())

# parent=[0]*(n+1)
# edges=[]
# result=0

# for i in range(1, n+1):
#     parent[i]=i

# for _ in range(m):
#     x, y, z=map(int, sys.stdin.readline().split()) # x번 집과 y번 집 사이에 양방향 도로가 있으며, 그 도로의 길이가 z
#     edges.append((z, x, y))

# edges.sort()
# total=0

# for edge in edges:
#     cost, a, b=edge
#     total+=cost
#     if find_parent(parent, a)!=find_parent(parent, b):
#         union_parent(parent, a, b)
#         result+=cost

# print(total-result) # 전체 가로등을 켜는 비용 - 최소 비용

# 2020년 12월 21일 풀이

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

n, m=map(int, sys.stdin.readline().split())

parent=[0]*(n+1)
edges=[]
result=0

for i in range(1, n+1):
    parent[i]=i

for _ in range(m):
    x, y, z=map(int, sys.stdin.readline().split())
    edges.append((z, x, y))

edges.sort()
total=0

for edge in edges:
    cost, a, b=edge
    total+=cost
    if findParent(parent, a)!=findParent(parent, b):
        unionParent(parent, a, b)
        result+=cost
    
print(total-result)