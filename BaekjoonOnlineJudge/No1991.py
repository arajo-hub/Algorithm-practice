# 전위 순회(preorder) : 부모 -> 왼쪽 -> 오른쪽
# 중위 순회(inorder) : 왼쪽 -> 부모 -> 오른쪽
# 후위 순회(postorder) : 왼쪽 -> 오른쪽 -> 부모

import sys

n = int(sys.stdin.readline())

graph = [[0]*3 for _ in range(26)] # 노드의 개수 최대 26개

# 전위 순회(preorder)
def preorder(start):
    print(start, end="")
    if graph[ord(start) - 65][1] != ".":
        preorder(graph[ord(start) - 65][1])
    if graph[ord(start) - 65][2] != ".":
        preorder(graph[ord(start) - 65][2])

# 중위 순회(inorder)
def inorder(start):
    if graph[ord(start) - 65][1] != ".":
        inorder(graph[ord(start) - 65][1])
    print(start, end="")
    if graph[ord(start) - 65][2] != ".":
        inorder(graph[ord(start) - 65][2])

# 후위 순회(postorder)
def postorder(start):
    if graph[ord(start) - 65][1] != ".":
        postorder(graph[ord(start) - 65][1])
    if graph[ord(start) - 65][2] != ".":
        postorder(graph[ord(start) - 65][2])
    print(start, end="")

for _ in range(n):
    center_node, left_node, right_node = map(str, sys.stdin.readline().split())
    standard = ord(center_node) - 65
    graph[standard][0], graph[standard][1], graph[standard][2] = center_node, left_node, right_node

preorder("A")
print()
inorder("A")
print()
postorder("A")

# https://pacific-ocean.tistory.com/322