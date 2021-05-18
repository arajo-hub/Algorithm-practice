import sys

# 도시의 개수
n = int(sys.stdin.readline())

# 버스의 개수
m = int(sys.stdin.readline())

INF = 100000000

matrix = [[INF] * n for _ in range(n)]

for _ in range(m):
    # a 도시에서 b 도시로 가는 비용 c
    a, b, c = map(int, sys.stdin.readline().split())
    if matrix[a-1][b-1] > c:
        matrix[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for each in matrix:
    for second in each:
        if second == INF:
            print(0, end = ' ')
        else:
            print(second, end = ' ')
    print()