from itertools import combinations
import sys

n=int(sys.stdin.readline())
board=[] # 복도 정보
teachers=[] # 선생님의 위치 정보
spaces=[] # 빈 공간의 위치 정보

for i in range(n):
    board.append(list(sys.stdin.readline().split()))
    for j in range(n):
        if board[i][j]=='T':
            teachers.append((i, j))
        if board[i][j]=='X': # 장애물을 설치할 수 있는 빈 공간을 저장한다.
            spaces.append((i, j))

def watch(x, y, direction):
    if direction==0: # 서쪽으로 감시
        while y>=0:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            y-=1
    if direction==1: # 동쪽으로 감시
        while y<n:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            y+=1
    if direction==2: # 북쪽으로 감시
        while x>=0:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            x-=1
    if direction==3: # 남쪽으로 감시
        while x<n:
            if board[x][y]=='S': # 학생이 있는 경우
                return True
            if board[x][y]=='O': # 장애물이 있는 경우
                return False
            x+=1
    return False

def process():
    for x, y in teachers:
        for i in range(4): # 네 방향에 대해서 감시하는 경우를 탐색
            if watch(x, y, i):
                return True
    return False

find=False

for data in combinations(spaces, 3): # 빈 공간 세 개를 고르는 모든 조합을 확인한다.
    for x, y in data:
        board[x][y]='O' # 장애물을 설치한다.
    if not process(): # 학생을 한 명도 못 찾은 경우
        find=True
        break
    for x, y in data: # 설치한 장애물을 다시 없앤다.
        board[x][y]='X'

if find:
    print('YES')
else:
    print('NO')