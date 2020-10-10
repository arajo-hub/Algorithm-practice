from collections import deque
INF = 1e9

n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dist = [[-1] * n for _ in range(n)] # 거리를 담는 리스트. -1은 도달할 수 없다는 의미
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0 # 현재 위치에서의 거리는 0
    while q:
        x, y = q.popleft()
        for i in range(4): # 네 방향 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n: # n범위 안에 있고,
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size: # 전진할 칸이 초기상태이고(-1), 지금 사이즈보다 작다면
                    dist[nx][ny] = dist[x][y] + 1 # 전진. 거리를 1 늘려준다.
                    q.append((nx, ny)) # 그리고 q에 새로운 위치를 담고 계속 진행한다.
    return dist

def find(dist): # 먹을 물고기를 찾는다.
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                if dist[i][j] < min_dist: # 가장 가까운 물고기 한 마리만 선택
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF: # 먹을 수 있는 물고기가 없다면 None을 반환한다.
        return None
    else:
        return x, y, min_dist # 먹을 물고기의 위치와 최단거리

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1
        if ate >= now_size:
            now_size += 1
            ate = 0