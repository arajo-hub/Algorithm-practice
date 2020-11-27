# from collections import deque
# import sys

# N, L, R=map(int, sys.stdin.readline().split())

# # 전체 나라의 정보를 입력한다.
# nations=[]
# for _ in range(N):
#     nations.append(list(map(int, sys.stdin.readline().split())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]

# def process(x, y, index):
#     united = [] # (x, y)위치와 같은 연합만 담는 리스트
#     united.append((x, y))
#     q = deque()
#     q.append((x, y))
#     union[x][y] = index # 현재 연합에 번호 할당
#     summary = nations[x][y] # 현재 연합의 전체 인구 수
#     count = 1 # 현재 연합의 국가 수
#     # 큐가 빌 때까지 반복(BFS)
#     while q:
#         x, y = q.popleft()
#         # 현재 위치에서 4가지 방향을 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
#                 if L <= abs(nations[nx][ny] - nations[x][y]) <= R: # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
#                     q.append((nx, ny)) # 연합에 추가
#                     union[nx][ny] = index # 옆에 있는 나라에도 연합 번호 할당
#                     summary += nations[nx][ny] # 인구수 더해주고
#                     count += 1 # 연합 국가수 +1
#                     united.append((nx, ny))
#     # 연합 국가끼리 인구를 분배
#     for i, j in united:
#         nations[i][j] = summary // count

# total_count = 0

# while True:
#     union = [[-1] * N for _ in range(N)]
#     index = 0
#     for i in range(N):
#         for j in range(N):
#             if union[i][j] == -1:
#                 process(i, j, index)
#                 index += 1
#     if index == N * N:
#         break
#     total_count += 1

# print(total_count)

# 2020년 11월 27일 풀이

from collections import deque
import sys

# 국경선을 공유하는 두 나라의 인구 차이가 l명 이상, r명 이하라면 각 칸의 인구수는 연합의 인구수/연합을 이루고 있는 칸의 개수(소수점 버림)
# 인구 이동이 몇 번 발생하는지?

n, l, r=map(int, sys.stdin.readline().split())

nation=[]
for i in range(n):
    nation.append(list(map(int, sys.stdin.readline().split()))) # 인구수 정보 넣기

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count=0


def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = nation[x][y]
    count = 1
    while q:
        x, y=q.popleft()
        for i in range(4):
            nx, ny=x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and union[nx][ny]==-1:
                if l<=abs(nation[x][y]-nation[nx][ny])<=r:
                    q.append((nx, ny))
                    union[nx][ny]=index
                    summary+=nation[nx][ny]
                    count+=1
                    united.append((nx, ny))
    for j, k in united:
        nation[j][k]=summary//count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)