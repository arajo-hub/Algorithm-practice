from collections import deque
m, n = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] # dx, dy를 순서대로 결합해보면 [하, 상, 좌, 우]
for i in range(n):
    s.append(list(map(int, input().split())))

def bfs(): # bfs함수를 이용하여 상, 하, 좌, 우를 검사하여 0을 찾아가는 과정
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < m and s[x][y] == 0: # 창고의 범위 내에서 익은 토마토의 상, 하, 좌, 우 중에 안 익은 토마토가 있다면,
                s[x][y] = s[a][b] + 1 # 기준이 되는 값에 1을 더해서 상, 하, 좌, 우에 넣어준다.
                queue.append([x, y]) # 그리고 위의 과정에서 익게 된 토마토의 좌표를 queue에 넣어준다.

for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j]) # 익은 토마토의 위치를 queue에 넣는다.

bfs()
isTrue = False
result = -2

for i in s:
    for j in i:
        if j == 0:
            isTrue = True
        result = max(result, j)

if isTrue == True: # bfs를 실행하고나서도 0이 있다면 -1을 출력
    print(-1)
elif result == -1: # 가장 큰 값이 -1이면 0을 출력
    print(0)
else: # 둘 다 아니라면 제일 큰 값에 -1을 한 값을 출력
    print(result - 1)