import sys

N, M=map(int, sys.stdin.readline().split())

maps=[]
for i in range(N): # 지도 정보를 입력한다.
    temp=list(map(int, sys.stdin.readline().split()))
    maps.append(temp)

new_maps=[[0]*M for _ in range(N)] # 벽을 설치하고 난 뒤의 맵

# 네 방향 이동 리스트
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def virus(x, y):
    for k in range(4):
        new_x, new_y=x+dx[k], y+dy[k]
        if 0<=new_x<N and 0<=new_y<M: # new_x, new_y가 맵 내의 위치인지 확인하고
            if new_maps[new_x][new_y]==0: # 빈칸이라면
                new_maps[new_x][new_y]=2 # 바이러스로 바꿔준다.
                virus(new_x, new_y) # new_x, new_y의 사방도 바이러스로 바꿔준다.

def count0():
    answer=0
    for i in new_maps:
        answer+=i.count(0)
    return answer

result=0
def dfs(count):
    global result
    if count==3:
        for i in range(N):
            for j in range(M):
                new_maps[i][j]=maps[i][j]
        for i in range(N):
            for j in range(M):
                if new_maps[i][j]==2:
                    virus(i, j)
        result=max(result, count0())
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j]==0:
                maps[i][j]=1
                count+=1
                dfs(count)
                maps[i][j]=0
                count-=1

dfs(0)
print(result)