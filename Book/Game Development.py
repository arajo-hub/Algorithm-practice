# import sys

# N, M=map(int, sys.stdin.readline().split()) # 맵의 가로길이 N, 세로길이 M을 입력한다.

# maps=[[0]*M for _ in range(N)]

# # 캐릭터의 위치 x, y와 바라보고 있는 방향 heading을 입력한다.
# # heading은 방향에 따라 0(북), 1(동), 2(남), 3(서)의 값을 갖는다.
# x, y, heading=map(int, sys.stdin.readline().split())
# maps[x][y]=1 # 위에서 입력한 캐릭터의 위치는 이미 가보았던 곳으로 표시(1)한다.

# # 맵 정보를 입력한다.
# # 0은 육지, 1은 바다를 나타낸다.
# array=[]
# for i in range(N):
#     array.append(list(map(int, sys.stdin.readline().split())))


# # 방향 heanding에 따른 x, y의 변화값을 나타낸다.
# # [0] 북쪽으로 갈 경우, 리스트 특성상 그전 리스트(x-1)의 동일 위치 값으로 이동해야 한다.
# # [1] 동쪽으로 갈 경우, 리스트 특성상 동일 리스트의 오른쪽으로 한 자리 옮긴 값(y+1)으로 이동해야 한다.
# # [2] 남쪽으로 갈 경우, 리스트 특성상 그다음 리스트(x+1)의 동일 위치 값으로 이동해야 한다.
# # [3] 서쪽으로 갈 경우, 리스트 특성상 동일 리스트의 왼쪽으로 한 자리 옮긴 값(y-1)으로 이동해야 한다.
# # x, y는 좌표를 나타내기도 하지만, 리스트의 인덱스로 활용할 수 있다는 점을 잊으면 안된다.
# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]

# # 문제에서 제시한 조건은 현재 방향을 기준으로 왼쪽 방향으로 전진하는 것이다.
# # 현재 방향을 이 함수를 통해 왼쪽 방향으로 돌려주고,
# # 이에 따라 전진한 새로운 위치는 위의 heading에 따른 x, y의 변화값을 이용하여 구한다.
# def left():
#     global heading
#     heading-=1 #
#     if heading==-1: # 방향은 네 방향이기 때문에 0에서 1을 빼면 3으로 돌아와야 한다.
#         heading=3

# cnt=1
# turn_time=0 # 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우를 식별해내야 하므로 turn_time을 생성해준다.

# while True:
#     left() # 현재 바라보는 방향에서 왼쪽으로 회전한다.
#     new_x=x+dx[heading] # 새로운 위치좌표 x와
#     new_y=y+dy[heading] # 새로운 위치좌표 y를 구한다.

#     if maps[new_x][new_y]==0 and array[new_x][new_y]==0: # 새로운 위치가 육지이면서 아직 가보지 않은 곳이면
#         maps[new_x][new_y]=1 # 가보았던 곳이라고 표시를 해주고
#         x, y=new_x, new_y # 현재위치를 새로운 위치로 옮긴다.
#         cnt+=1 # 한 번 이동했으므로 cnt에 1을 더해준다.
#         turn_time=0 # 이 부분에 turn_time이 있는 이유는 여러 방향으로 돌다가 마침내 이동할 곳을 찾았다면 turn_time을 0으로 초기화하여 다시 사용해야 하기 때문이다.
#         continue
#     else: # 새로운 위치가 바다이거나 가봤던 곳이라면
#         turn_time+=1 # turn_time을 1 올려준다.
#     if turn_time==4: # 네 방향 모두 바다이거나 가봤던 곳인 경우,
#         new_x, new_y=x-dx[heading], y-dy[heading] # 뒤쪽 방향으로 이동한다고 했을 때,
#         if array[new_x][new_y]==0: # 새로운 위치가 가봤는지, 안 가봤는지 여부에 상관없이 육지라면
#             x, y=new_x, new_y # 이동하고
#         else: # 뒤로 갈 수 없다면(=뒤쪽이 바다일 경우)
#             break # 반복문은 끝난다.
#         turn_time=0

# print(cnt)

# # 이 문제를 풀면서 굳이 맵을 maps와 array 두 가지로 나누어서 나타낼 필요가 있는가 의문이 들었다.
# # 그런데 생각해보니 네 방향 모두 가봤던 곳이거나 바다인 경우 뒤쪽 방향으로 이동한다는 조건이 있는데 이 조건을 충족시키려면 어쩔 수 없이 두 가지가 필요하겠다는 생각이 들었다.
# # 뒤쪽 방향으로 이동할 경우는 그 뒤쪽 방향의 새로운 위치가 가봤는지, 안 가봤는지가 중요한 게 아니다.
# # 바다만 아니라면 이동할 수 있는 것이다.
# # 이미 가봤던 곳이라도 이동 후, 그곳에서 왼쪽방향부터 차례로 나갈 수 있는 방향을 탐색하는 것이다.
# # 바다만 아니라면 이동할 수 있다는 말은 곧 뒤쪽방향이 바다일 때 비로소 모든 상황이 종료된다는 말이다.
# # 바다인지 아닌지 식별할 수 있어야 한다는 말인데, 그래서 굳이 맵을 maps와 array로 나눈 것이다.

# 2020년 10월 20일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())
maps=[[0]*m for _ in range(n)]

x, y, direc=map(int, sys.stdin.readline().split())
maps[x][y]=1

array=[]
for i in range(m):
    array.append(list(map(int, sys.stdin.readline().split())))

# 북쪽은 0, 서쪽은 1, 남쪽은 2, 동쪽은 3
def getDirection():
    global direc
    direc-=1
    if direc==-1:
        direc=3


dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

cnt=1
turn=0
while True:
    getDirection()
    new_x, new_y=x+dx[direc], y+dy[direc]
    if maps[new_x][new_y]==0 and array[new_x][new_y]==0:
        maps[new_x][new_y]=1
        x, y=new_x, new_y
        cnt+=1
        turn=0
        continue
    else:
        turn+=1
    if turn==4:
        new_x, new_y=x-dx[direc], y-dy[direc]
        if array[new_x][new_y]==0:
            x, y=new_x, new_y
        else:
            break
        turn=0

print(cnt)