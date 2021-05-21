import sys, math, heapq

def find(x):
    global parent

    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    global parent, rank

    x = find(x)
    y = find(y)

    if x == y:
        return False
    
    if rank[x] < rank[y]:
        x, y = y, x

    parent[y] = x

    if rank[x] == rank[y]:
        rank[y] += 1
    
    return True

def calc_diff(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

# 우주신들의 개수 n, 이미 연결된 신들과의 통로의 개수 m
n, m = map(int, sys.stdin.readline().split())

answer = 0
parent = [0] * (n+1)
rank = [1] * (n+1)

for i in range(1, n+1):
    parent[i] = i

god = [0]

for _ in range(n):
    god.append(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

q = []
for i in range(1, n):
    for j in range(i+1, n+1):
        diff = calc_diff(god[i], god[j])
        heapq.heappush(q, [diff, i, j])

while q:
    cost, a, b = heapq.heappop(q)

    if union(a, b):
        answer += cost
    
print("%0.2f" % answer)