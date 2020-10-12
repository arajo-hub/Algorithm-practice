import sys

n, m, k = map(int, sys.stdin.readline().split())

array = []
for i in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

directions = list(map(int, sys.stdin.readline().split()))

smell = [[[0, 0]] * n for _ in range(n)] # [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 리스트

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, sys.stdin.readline().split()))) # 회전의 우선순위를 저장한다.

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0: # 냄새가 존재한다면
                smell[i][j][1] -= 1 # 시간을 1만큼 줄인다.
            if array[i][j] != 0: # 상어가 존재하는 해당 위치의 냄새를 k로 설정한다.
                smell[i][j] = [array[i][j], k]

def move(): # 모든 상어를 이동시킨다.
    new_array = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if array[x][y] != 0: # 상어가 존재하는 경우
                direction = directions[array[x][y] - 1]
                found = False
                for index in range(4): # 네 방향 중에 냄새가 존재하지 않는 경우가 있는지 확인한다.
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 존재하지 않는 곳이라면
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index] # 새로운 방향으로 이동시킨다.
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]:
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    if time >= 1000: # 1000초가 지날 때까지 끝나지 않았다면
        print(-1)
        break