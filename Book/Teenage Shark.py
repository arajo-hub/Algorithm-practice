import copy
import sys

array=[[None]*4 for _ in range(4)]

for i in range(4):
    data=list(map(int, sys.stdin.readline().split()))
    for j in range(4): # 4마리의 물고기를 하나씩 확인하여
        array[i][j]=[data[j*2], data[j*2+1]-1] # [물고기의 번호, 방향]을 저장한다.

# 8개의 방향
dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction): # 현재 위치에서 왼쪽으로 회전시키는 함수
    return (direction+1)%8

result=0

def find_fish(array, index): # 특정한 물고기의 위치를 찾는 함수
    for i in range(4):
        for j in range(4):
            if array[i][j][0]==index:
                return (i, j)
    return None

def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17): # 1부터 16번까지의 물고기를 확인
        position=find_fish(array, i)
        if position!=None:
            x, y=position[0], position[1]
            direction=array[x][y][1]
            # 물고기의 방향을 계속 왼쪽으로 회전시키며 이동이 가능한지 확인한다.
            for j in range(8):
                nx=x+dx[direction]
                ny=y+dy[direction]
                if 0<=nx and nx<4 and 0<=ny and ny<4:
                    if not (nx==now_x and ny==now_y):
                        array[x][y][1]=direction
                        array[x][y], array[nx][ny]=array[nx][ny], array[x][y]
                        break
                direction=turn_left(direction)

def get_possible_positions(array, now_x, now_y): # 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치를 반환하는 함수
    positions=[]
    direction=array[now_x][now_y][1]
    for i in range(4):
        now_x+=dx[direction]
        now_y+=dy[direction]
        if 0<=now_x and now_x<4 and 0<=now_y and now_y<4:
            if array[now_x][now_y]!=-1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array=copy.deepcopy(array)
    total+=array[now_x][now_y][0] # 현재 위치의 물고기를 먹고 시작한다.
    array[now_x][now_y][0]=-1 # 이미 먹은 물고기이므로 -1로 바꿔준다.
    move_all_fishes(array, now_x, now_y) # 전체 물고기를 이동시켜주고
    positions=get_possible_positions(array, now_x, now_y) # 상어가 이동 가능한 위치를 찾는다.
    if len(positions)==0: # 이동할 수 있는 위치가 없다면
        result=max(result, total) # 최댓값 저장하고 끝난다.
        return
    # 모든 이동할 수 있는 위치로 재귀함수를 수행한다.
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

dfs(array, 0, 0, 0)
print(result)