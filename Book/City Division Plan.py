# import sys

# def find_parent(parent, x):
#     if parent[x]!=x:
#         parent[x]=find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a=find_parent(parent, a)
#     b=find_parent(parent, b)
#     if a>b:
#         parent[b]=a
#     else:
#         parent[a]=b

# N, M=map(int, sys.stdin.readline().split())
# citymap=[i for i in range(N+1)]

# edges=[]
# result=0

# for i in range(M):
#     A, B, C=map(int, sys.stdin.readline().split()) # A집과 B집을 연결하는 길의 유지비는 C
#     edges.append((C, A, B))

# edges.sort()
# last=0

# for edge in edges:
#     cost, a, b=edge
#     if find_parent(citymap, a)!=find_parent(citymap, b):
#         union_parent(citymap, a, b)
#         result+=cost
#         last=cost # last는 간선 중에서 가장 비용이 큰 간선이 된다. edges를 sort해놓았기 때문.

# print(result-last)

# 2020년 11월 6일 풀이

import sys

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

v, e=map(int, sys.stdin.readline().split())
parent=[0]*(v+1)

edges=[]
result=0

for i in range(1, v+1):
    parent[i]=i

for _ in range(e):
    a, b, cost=map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()
last=0

for edge in edges:
    cost, a, b=edge
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        result+=cost
        last=cost

print(result-last)