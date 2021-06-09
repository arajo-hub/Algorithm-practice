# 루트가 있는 트리(rooted tree)가 주어지고,
# 그 트리 상의 두 정점이 주어질 때
# 그들의 가장 가까운 공통 조상은 다음과 같이 정의된다.

# 두 노드의 가장 가까운 공통 조상
# 두 노드를 모두 자손으로 가지면서 깊이가 가장 깊은(즉 두 노드에 가장 가까운) 노드

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())

    parent_node = [0 for _ in range(N+1)]

    for _ in range(N-1):
        p, c = map(int, sys.stdin.readline().split())
        parent_node[c] = p

    A, B = map(int, sys.stdin.readline().split())
    a_parent = [A]
    b_parent = [B]

    while parent_node[A]:
        a_parent.append(parent_node[A])
        A = parent_node[A]
    
    while parent_node[B]:
        b_parent.append(parent_node[B])
        B = parent_node[B]
    
    a_level = len(a_parent) - 1
    b_level = len(b_parent) - 1

    while a_parent[a_level] == b_parent[b_level]:
        a_level -= 1
        b_level -= 1
    
    print(a_parent[a_level + 1])