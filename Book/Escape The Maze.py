from collections import deque
import sys

N, M=map(int, sys.stdin.readline().split()) # 미로의 세로 길이 N, 가로 길이 M을 입력한다.

maze=[]
maze=[list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(N)] # 미로의 정보를 입력한다.

# 미로의 [0, 0]에서 시작하여 [N, M]까지 갈 경우,
# 필요한 이동방식은 두 가지다.
# 오른쪽으로 가거나, 아래쪽으로 가거나.
# 이 문제에는 최소이동횟수를 구하는 것이기 때문에
# 위로 가거나 왼쪽으로 가는 경우는 최소라는 조건을 만족할 수 없다.
dx=[1, 0]
dy=[0, 1]

def dfs(x, y):
    queue=deque()
    queue.append((x, y))
    while queue: # queue가 빈 상태가 될 때까지 아래의 과정을 반복한다.
        x, y=queue.popleft()
        for i in range(2): # 차례대로 1. 오른쪽으로 이동하는 경우 2. 아래쪽으로 이동하는 경우를 테스트한다.
            new_x, new_y=x+dx[i], y+dy[i] # 이동했을 경우의 새로운 위치를 구하고
            if new_x<0 or new_y<0 or new_x>=N or new_y>=M: # 미로 범위 안에 속하지 않으면 continue를 한다.
                continue
            if maze[new_x][new_y]==0: # 새로운 위치가 괴물이 있는 곳이라면
                continue # continue를 하고,
            if maze[new_x][new_y]==1: # 괴물이 없는 곳이라면
                maze[new_x][new_y]=maze[x][y]+1 # 새로운 위치의 값을 기존값+1해준다. 이 과정에서 최소이동횟수가 계산된다.
                queue.append((new_x, new_y)) # queue에 nx, ny를 추가한다.
    return maze[N-1][M-1]

print(dfs(0, 0))