def bfs(now_x, now_y, final_x, final_y):

    q=deque()

    # 시작점을 지나온 것으로 처리한다.
    q.append((now_x, now_y))
    board[now_x][now_y]=1

    while q:
        x, y=q.popleft() # 좌표를 꺼내서
        if x==final_x and y==final_y: # 목적지에 도착
            print(board[final_x][final_y]-1)
            return
        # 목적지가 아닌 곳이면
        for i in range(8): # 8개 방향 탐색
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<board_length and 0<=ny<board_length and board[nx][ny]==0: # 새로운 위치가 이동할 수 있는 위치이면 그 위치로 이동
                q.append((nx, ny))
                board[nx][ny]=board[x][y]+1

from collections import deque
import sys

tc = int(sys.stdin.readline())

# 나이트가 이동할 수 있는 8개 방향
dx=[-2, -2, -1, -1, 1, 1, 2, 2]
dy=[-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(tc): # 테스트 케이스 개수만큼 반복
    # 체스판 길이
    board_length = int(sys.stdin.readline())
    # 현재 위치
    now_x, now_y = map(int, sys.stdin.readline().split())
    # 목표로 하는 최종 위치
    final_x, final_y = map(int, sys.stdin.readline().split())

    # 체스판을 만든다.
    board=[[0]*board_length for i in range(board_length)]

    bfs(now_x, now_y, final_x, final_y)