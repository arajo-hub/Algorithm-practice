import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    q = deque([[0, 0, 1]])
    visited = [[[0] * 2 for i in range(m)] for i in range(n)]
    visited[0][0][1] = 1

    while q:
        
        x, y, broken = q.popleft()

        # 목적지에 도착하면 끝
        if x == n - 1 and y == m - 1:
            return visited[x][y][broken]
        
        # 목적지에 아직 도착하지 않은 경우
        # 네 방향 탐색
        for i in range(4):

            # 새로운 위치로 갈 수 있는지 없는지
            nx = x + dx[i]
            ny = y + dy[i]

            # 지도 내의 범위이고
            if 0 <= nx < n and 0 <= ny < m:

                # 벽이 있지만 뚫을 수 있다면
                if s[nx][ny] == 1 and broken == 1:
                    # 벽을 뚫는다.
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    # 그리고 그 위치를 큐에 넣는다.
                    # 끝의 0은 이미 벽을 한 번 뚫었다는 의미
                    q.append([nx, ny, 0])
                
                # 벽이 없고 방문한 적이 없다면
                elif s[nx][ny] == 0 and visited[nx][ny][broken] == 0:

                    # 방문한 것으로 해준다.
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    q.append([nx, ny, broken])
    return -1
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, list(input().strip()))))
print(bfs())