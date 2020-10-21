# import sys

# N, M=map(int, sys.stdin.readline().split()) # 얼음 틀의 세로 길이 N과 가로 길이 M을 입력한다.

# # ice리스트를 만들고, 맵의 정보를 저장한다.
# ice=[]
# for i in range(N):
#     ice.append(list(map(int, sys.stdin.readline().strip('\n'))))

# # 상하좌우 구멍이 뚫려 있는지 체크하여 구멍이 있으면 True 없으면 False를 반환하는 함수를 만든다.
# def dfs(x, y):
#     if x<0 or x>=N or y<0 or y>=M:
#         return False
#     if ice[x][y]==0: # ice[x][y]가 구멍이 뚫려 있다면
#         ice[x][y]=1 # 이미 방문한 곳으로 표시를 해놓고 재귀함수를 이용하여 상하좌우를 탐색한다.
#         dfs(x+1, y) # 우
#         dfs(x-1, y) # 좌
#         dfs(x, y+1) # 하
#         dfs(x, y-1) # 상
#         return True
#     return False

# result=0
# for i in range(N):
#     for j in range(M):
#         if dfs(i, j)==True:
#             print(ice)
#             result+=1

# print(result)

# # 내가 입력한 ice
# # [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

# # dfs(0, 0)
# # ice[0, 0]은 0이므로 True를 반환하고, ice[0, 0]은 1로 바뀐다. result는 1 올라간다.
# # dfs(1, 0)과 dfs(0, 1)을 실행하는데, 깊이 우선 탐색이므로 먼저 dfs(1, 0)에서 끝까지 가야 한다.
# # dfs(1, 0)은 0이므로 True를 반환하고 dfs(2, 0)과 dfs(1, 1)을 실행하는데 깊이 우선 탐색이므로 dfs(2, 0)을 먼저 실행한다. ice[1, 0]은 1로 바뀐다.
# # dfs(2, 0)은 1이므로 False를 반환하고 끝난다.
# # dfs(1, 1)은 0이므로 True를 반환하고 dfs(2, 1)과 dfs(1, 2)을 실행한다. ice[1, 1]은 1로 바뀐다.
# # dfs(2, 1)은 1이므로 False를 반환하고 끝난다.
# # dfs(1, 2)은 0이므로 True를 반환하고 dfs(2, 2)과 dfs(1, 3)을 실행한다. ice[1, 2]는 1로 바뀐다.
# # dfs(2, 2)은 1이므로 False를 반환하고 끝난다.
# # dfs(1, 3)은 1이므로 False를 반환하고 끝난다.
# # dfs(1, 0)이 끝났으므로 dfs(0, 1)을 실행한다.
# # dfs(0, 1)은 0이므로 True를 반환하고 dfs(0, 2)을 실행한다. ice[0, 1]은 1로 바뀐다.
# # dfs(0, 2)는 1이므로 False를 반환하고 끝난다.

# # 바뀌기 전 : [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
# # 바뀌고 난 후 : [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]



# # dfs(0, 1)
# # dfs(0, 1)는 위의 경우에서 1로 바뀌었으므로 False를 반환하고 끝난다.



# # dfs(0, 2)
# # dfs(0, 2)도 1이므로 False를 반환하고 끝난다.



# # dfs(0, 3)
# # dfs(0, 3)도 1이므로 False를 반환하고 끝난다.



# # dfs(0, 4)
# # dfs(0, 4)는 0이므로 True를 반환하고, ice[0, 4]는 1로 바뀐다. result는 1 올라간다.
# # dfs(1, 4)과 dfs(0, 5), dfs(0, 3)을 실행한다.
# # dfs(1, 4)은 1이므로 False를 반환하고 끝난다.
# # dfs(0, 5)은 1이므로 False를 반환하고 끝난다.
# # dfs(0, 3)은 1이므로 False를 반환하고 끝난다.
# # 바뀌기 전 : [[1, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
# # 바뀌고 난 후 : [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]



# # dfs(1, 0)
# # dfs(1, 0)은 1이므로 False를 반환하고 끝난다.



# # dfs(1, 1)부터 dfs(2, 4)까지는 전부 1이므로 False를 반환하고 끝난다.



# # dfs(3, 0)
# # dfs(3, 0)은 0이므로 True를 반환하고, ice[3, 0]는 1로 바뀐다. result는 1 올라간다.
# # dfs(3, 1)을 실행한다.
# # dfs(3, 1)은 0이므로 True를 반환하고, ice[3, 1]은 1로 바뀐다.
# # dfs(3, 2)을 실행한다.
# # dfs(3, 2)은 0이므로 True를 반환하고, ice[3, 2]은 1로 바뀐다.
# # dfs(3, 3)을 실행한다.
# # dfs(3, 3)은 0이므로 True를 반환하고, ice[3, 3]은 1로 바뀐다.
# # dfs(3, 3)에서 상하좌우로 더 이상 실행할 경우의 수가 없으므로 dfs는 끝난다.
# # 바뀌기 전 : [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
# # 바뀌고 난 후 : [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

# 2020년 10월 21일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())

frame=[]
for i in range(n):
    frame.append(list(map(int, sys.stdin.readline().strip('\n'))))

cnt=0
time=0
def dfs(x, y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if frame[x][y]==0:
        frame[x][y]=1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i, j)==True:
            result+=1

print(result)