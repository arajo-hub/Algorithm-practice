import sys

n, m = map(int, sys.stdin.readline().split())
a = []
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
b = []
for _ in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))

box = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for h in range(m):
            box[i][j] += a[i][h] * b[h][j]

for t in box:
    for f in t:
        print(f, end = ' ')
    print()

# 출처 : https://claude-u.tistory.com/262