# import sys
# import heapq

# def find_parent(parent, x):
#     if parent[x]!=x: # 자기자신으로 초기화되어있지 않다면
#         parent[x]=find_parent(parent, parent[x]) # 루트노드를 찾아서
#     return parent[x] # 반환

# def union_parent(parent, a, b):
#     a=find_parent(parent, a) # a의 루트노드를 반환하고,
#     b=find_parent(parent, b) # b의 루트노드를 반환해서
#     # 작은 쪽의 값으로 바꿔주기
#     if a<b:
#         parent[b]=a
#     else:
#         parent[a]=b

# n, m=map(int, sys.stdin.readline().split())
# parent=[0]*(n+1)

# for k in range(1, n+1):
#     parent[k]=k # 부모를 자기자신으로 초기화

# for i in range(n):
#     data=list(map(int, sys.stdin.readline().split()))
#     for j in range(n):
#         if data[j]==1: # 1로 입력된 경우(=두 여행지가 연결된 경우)는
#             union_parent(parent, i+1, j+1) # union_parent 수행

# plan=list(map(int, sys.stdin.readline().split())) # 여행계획 입력

# result=True

# for j in range(m-1): # 여행계획에 속하는 모든 노드의 루트가 동일한지 확인
#     if find_parent(parent, plan[j])!=find_parent(parent, plan[j+1]):
#         result=False

# if result:
#     print("YES")
# else:
#     print("NO")

# 2020년 12월 18일 풀이

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

import heapq
import sys

n, m=map(int, sys.stdin.readline().split()) # 여행지의 수 n, 여행 계획에 속한 도시의 수 m
parent=[0]*(n+1)

for j in range(1, n+1):
    parent[j]=j

graph=[[]*(n+1) for _ in range(n+1)]
q=[]

for i in range(n):
    data=list(map(int, sys.stdin.readline().split()))
    for k in range(n):
        if data[k]==1:
            unionParent(parent, i+1, k+1)

plan=list(map(int, sys.stdin.readline().split()))

result=True

for h in range(m-1):
    if findParent(parent, plan[h])!=findParent(parent, plan[h+1]):
        result=False

if result:
    print("YES")
else:
    print("NO")