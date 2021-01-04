import sys

def horizontal_possible(num, x):
    if num in sudoku[x]: # 같은 줄에 숫자가 있다면
        return False
    else:
        return True

def vertical_possible(num, y):
    for i in range(9):
        if num==sudoku[i][y]:
            return False
    return True

def square_possible(num, x, y):
    nx=x//3*3
    ny=y//3*3

    for i in range(nx, nx+3):
        for j in range(ny, ny+3):
            if sudoku[i][j]==num:
                return False
    return True

# for k in range(9): # 가로
#     for j in range(9): # 세로
#         if sudoku[k][j]==0: # 숫자를 채워야 할 곳을 만나면
#             for num in range(1, 10): # 9개의 숫자 중 어떤 숫자를 채워야할지 for문을 돌린다.
#                 if horizontal_possible(num, k) and vertical_possible(num, j) and square_possible(num, k, j):
#                     sudoku[k][j]=num
#                 else:
#                     continue
#         else:
#             continue

# for p in sudoku:
#     print(*p)

def dfs(index):
    if index==len(zeros):
        for row in sudoku:
            for n in row:
                print(n, end=" ")
            print()
        sys.exit(0)
    else:
        for num in range(1, 10):
            nx=zeros[index][0]
            ny=zeros[index][1]
        
            if horizontal_possible(num, nx) and vertical_possible(num, ny) and square_possible(num, nx, ny):
                sudoku[nx][ny]=num
                dfs(index+1)
                sudoku[nx][ny]=0

sudoku=[]

for i in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))

zeros=[(i, j) for i in range(9) for j in range(9) if sudoku[i][j]==0] # 0인 위치의 좌표를 모아놓은 리스트
dfs(0)