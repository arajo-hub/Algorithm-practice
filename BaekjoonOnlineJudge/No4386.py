# n개의 별들을 이어서 별자리를 하나 만드는 문제
# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 함

import sys

def find(x):
    if x == root[x]:
        return x
    else:
        return find(root[x])
    
def union(a, b):
    root_a, root_b = find(a), find(b)
    root[root_b] = root_a

# 별의 개수
n = int(sys.stdin.readline())

stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

root = [each for each in range(n)]

costs = {} # dictionary

for i in range(n):
    for j in range(i+1, n):
        a = stars[i]
        b = stars[j]
        dist = round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 2)
        costs[(i, j)] = dist

costs = sorted(costs.items(), key = lambda x:x[1])

answer = 0

while costs:
    current = costs.pop(0)
    a, b = current[0]
    cost = current[1]

    if find(a) != find(b):
        answer += cost
        union(a, b)

print(answer)