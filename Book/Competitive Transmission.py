from collections import deque
import sys

N, K=map(int, sys.stdin.readline().split())

examiner=[] # 전체 실험관 정보
data=[] # 바이러스에 대한 정보

for i in range(N):
    examiner.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if examiner[i][j]!=0:
            data.append((examiner[i][j], 0, i, j))

data.sort()
q=deque(data)

S, X, Y=map(int, sys.stdin.readline().split())

# 동, 서, 남, 북으로 이동하는 경우
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]

while q:
    virus, s, x, y=q.popleft()
    if s==S:
        break
    for i in range(4):
        new_x, new_y=x+dx[i], y+dy[i]
        if 0<=new_x<N and 0<=new_y<N:
            if examiner[new_x][new_y]==0:
                examiner[new_x][new_y]=virus
                q.append((virus, s+1, new_x, new_y))