# n = int(input()) # 보드의 크기
# k = int(input()) # 사과의 개수
# data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
# info = [] # 방향 회전 정보

# # 맵 정보(사과 있는 곳은 1로 표시)
# for _ in range(k):
#     a, b = map(int, input().split())
#     data[a][b] = 1

# # 방향 회전 정보 입력
# l = int(input())
# for _ in range(l):
#     x, c = input().split()
#     info.append((int(x), c))

# # 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def turn(direction, c):
#     if c == "L":
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# def simulate():
#     x, y = 1, 1 # 뱀의 머리 위치
#     data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
#     direction = 0 # 처음에는 동쪽을 보고 있음
#     time = 0 # 시작한 뒤에 지난 '초' 시간
#     index = 0 # 다음에 회전할 정보
#     q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

#     while True:
#         nx = x + dx[direction]
#         ny = y + dy[direction]
#         # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
#         if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
#             # 사과가 없다면 이동 후에 꼬리 제거
#             if data[nx][ny] == 0:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#                 px, py = q.pop(0)
#                 data[px][py] = 0
#             # 사과가 있다면 이동 후에 꼬리 그대로 두기
#             if data[nx][ny] == 1:
#                 data[nx][ny] = 2
#                 q.append((nx, ny))
#         # 벽이나 뱀의 몸통과 부딪혔다면
#         else:
#             time += 1
#             break
#         x, y = nx, ny # 다음 위치로 머리를 이동
#         time += 1
#         if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
#             direction = turn(direction, info[index][1])
#             index += 1
#     return time

# print(simulate())

# 2020년 11월 18일 풀이

import sys

# 방향은 몇 칸을, 어느 방향으로 이동하는지 입력
# 뱀이 있는 위치는 2로 표시
# 사과가 없다면(0) 이동 후에 꼬리를 제거
# 사과가 있다면(1) 이동 후에 꼬리는 그대로 두고 머리만 이동
# 벽이나 뱀의 몸통과 부딪혔다면 초만 +1

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c)) # 이동할 시간, 방향

def turn(direction, c): # direction은 현재 방향, c는 회전하고자 하는 방향
    if c=='L': # 왼쪽으로 이동할 경우
        direction=(direction-1)%4
    else:
        direction=(direction+1)%4
    return direction

# 방향 동남서북(시계방향으로)
dx=[0, 1, 0, -1]
dy=[1, 0, -1, 0]
def simulate():
    x, y=1, 1 # 뱀의 초기 위치
    data[x][y]=2 # 뱀의 초기 위치에 뱀이 있다고 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while(True):
        nx, ny=x+dx[direction], y+dy[direction]
        if nx>=1 and nx<=n and ny>=1 and ny<=n and data[nx][ny]!=2:
            if data[nx][ny]==0:
                data[nx][ny]=2
                info.append((nx, ny))
                px, py=q.pop()
                data[px, py]=0
            if data[nx][ny]==1:
                data[nx][ny]=2
                info.append((nx, ny))
        else:
            time+=1
            break
        x, y=nx, ny
        time+=1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time