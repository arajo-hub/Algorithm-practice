# import sys

# N, M=map(int, sys.stdin.readline().split())

# maps=[]
# for i in range(N): # 지도 정보를 입력한다.
#     temp=list(map(int, sys.stdin.readline().split()))
#     maps.append(temp)

# new_maps=[[0]*M for _ in range(N)] # 벽을 설치하고 난 뒤의 맵

# # 네 방향 이동 리스트
# dx=[1, -1, 0, 0]
# dy=[0, 0, 1, -1]

# def virus(x, y):
#     for k in range(4):
#         new_x, new_y=x+dx[k], y+dy[k]
#         if 0<=new_x<N and 0<=new_y<M: # new_x, new_y가 맵 내의 위치인지 확인하고
#             if new_maps[new_x][new_y]==0: # 빈칸이라면
#                 new_maps[new_x][new_y]=2 # 바이러스로 바꿔준다.
#                 virus(new_x, new_y) # new_x, new_y의 사방도 바이러스로 바꿔준다.

# def count0():
#     answer=0
#     for i in new_maps:
#         answer+=i.count(0)
#     return answer

# result=0
# def dfs(count):
#     global result
#     if count==3:
#         for i in range(N):
#             for j in range(M):
#                 new_maps[i][j]=maps[i][j]
#         for i in range(N):
#             for j in range(M):
#                 if new_maps[i][j]==2:
#                     virus(i, j)
#         result=max(result, count0())
#         return
#     for i in range(N):
#         for j in range(M):
#             if maps[i][j]==0:
#                 maps[i][j]=1
#                 count+=1
#                 dfs(count)
#                 maps[i][j]=0
#                 count-=1

# dfs(0)
# print(result)

# 2020년 11월 23일 풀이

import sys

n, m=map(int, sys.stdin.readline().split()) # 지도의 세로 크기, 가로크기
maps=[] # 원래의 맵
new_maps=[[0]*m for _ in range(n)] # 벽을 설치하고 난 뒤의 맵

# 맵 정보를 넣는다.
for i in range(n):
    data=list(map(int ,sys.stdin.readline().split()))
    maps.append(data)

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

result=0

def virus(x, y): # 바이러스가 퍼지는 함수
    for i in range(4):
        nx, ny=x+dx[i], y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if new_maps[nx][ny]==0: # 갈 칸이 빈칸이라면
                new_maps[nx][ny]=2 # 그 칸을 바이러스로 바꿔주고
                virus(nx, ny) # 그 사방도 바이러스로 바꾼다.

def countZero(): # 0을 세는 함수
    answer=0
    for i in range(n):
        for j in range(m):
            if new_maps[i][j]==0:
                answer+=1
    return answer

def dfs(count):
    global result
    if count==3: # 벽이 3개 세워졌다면
        for i in range(n):
            for j in range(m):
                new_maps[i][j]=maps[i][j] # 원래 맵의 정보를 벽을 세우고 난 후의 맵에 옮긴다.
        # 그리고 각 위치에서 바이러스는 전파가 진행된다.
        for i in range(n):
            for j in range(m):
                if new_maps[i][j]==2:
                    virus(i, j)
        result=max(result, countZero())
        return
    for i in range(n):
        for j in range(m):
            if maps[i][j]==0: # 빈 공간에 벽을 세운다.
                maps[i][j]=1
                count+=1
                dfs(count)
                maps[i][j]=0
                count-=1

dfs(0)
print(result)