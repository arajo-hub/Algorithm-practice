import sys

sys.setrecursionlimit(10**9)

# 탐색할 네 방향
# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    
    # 마지막 칸이라면
    if x == m-1 and y == n-1:
        return 1 # 1 반환
    
    # 지나갔던 곳이라면
    if check[x][y] != -1:
        return check[x][y]
    
    check[x][y] = 0

    # 네 방향을 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            # 새로운 방향의 값이 현재보다 작다면
            if matrix[nx][ny] < matrix[x][y]:
                # 확인용 배열에 값을 누적
                check[x][y] += dfs(nx, ny)
    
    # 누적된 값 반환
    return check[x][y]

# 지도의 세로 크기 m, 가로 크기 n
m, n = map(int, sys.stdin.readline().split())

matrix = []
for _ in range(m):
    matrix.append(list(map(int, sys.stdin.readline().split())))

check = [[-1]*n for _ in range(m)]

# (0, 0)에서부터 시작
print(dfs(0, 0))