def rotate_a_matrix_by_90_degree(matrix): # 시계방향으로 90도 회전시키는 함수
    n=len(matrix)
    m=len(matrix[0])
    result=[[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=matrix[i][j]
    return result

def check(new_lock): # 열쇠가 맞는지 확인
    lock_length=len(new_lock)//3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j]!=1: # 열쇠와 자물쇠가 맞는다면 모두 1로 표시되기 때문에 new_lock[i][j]가 1이 아닐 경우 False를 리턴한다.
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)] # 자물쇠를 3배 크게 만든다.
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j] # 새로 만든 자물쇠에 입력받은 자물쇠를 같은 위치에 넣어준다.

    for rotation in range(4): # 4방향을 모두 검토한다.
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j] # 자물쇠의 빈 자리(0)에 열쇠가 딱 맞는다면 0이 1로 바뀌어 전부 1이 된다.
                if check(new_lock) == True:
                    return True
                for i in range(m): # 열쇠가 자물쇠에 맞지 않는다면 다시 열쇠를 빼준다.
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False