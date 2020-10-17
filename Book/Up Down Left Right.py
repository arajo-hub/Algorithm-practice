# import sys

# N=int(sys.stdin.readline())
# cmd=list(sys.stdin.readline().split())

# point=[1, 1]

# for i in range(len(cmd)):
#     if cmd[i]=='L':
#         if point[1]==1:
#             continue
#         else:
#             point[1]-=1
#     elif cmd[i]=='R':
#         if point[1]+1>N:
#             continue
#         else:
#             point[1]+=1
#     elif cmd[i]=='U':
#         if point[0]==1:
#             continue
#         else:
#             point[0]-=1
#     elif cmd[i]=='D':
#         if point[0]+1>N:
#             continue
#         else:
#             point[0]+=1

# print(*point)

# # 책 속의 풀이

# import sys
# n=int(sys.stdin.readline())
# x, y=1
# plans=sys.stdin.readline().split()

# # 격자형 구조를 주고 경로를 찾는 문제가 자주 있는데,
# # 이런 문제를 풀 때는 위의 풀이방식보다 아래의 풀이방식을 이용하는 습관을 들일 것.

# dx=[0, 0, -1, 1]
# dy=[-1, 1, 0, 0]
# move_types=['L', 'R', 'u', 'D']

# for plan in plans:
#     for i in range(len(move_types)):
#         if plan==move_types[i]:
#             nx=x+dx[i]
#             ny=y+dy[i]
#     if nx<1 or ny<1 or nx>n or ny>n:
#         continue
#     x, y=nx, ny

# print(x, y)

# 2020년 10월 17일 풀이

# import sys

# n=int(sys.stdin.readline())
# maps=[[0]*(n+1) for _ in range(n+1)]
# maps[1][1]=1

# cmd=list(sys.stdin.readline().split())

# x, y=1, 1
# for i in cmd:
#     if i=='R': # 오른쪽으로 한 칸 이동
#         new_x, new_y=x, y+1
#     elif i=='L': # 왼쪽으로 한 칸 이동
#         new_x, new_y=x, y-1
#     elif i=='U': # 위로 한 칸 이동
#         new_x, new_y=x-1, y
#     elif i=='D': # 아래로 한 칸 이동
#         new_x, new_y=x+1, y
#     if new_x>(n+1) or new_y>(n+1) or new_x<1 or new_y<1:
#         continue
#     x, y=new_x, new_y
#     maps[x][y]=1

# for j in maps:
#     print(j)

# print(x, y)

# 위 방법을 좀 더 발전시킨 풀이

import sys

n=int(sys.stdin.readline())

cmd=list(sys.stdin.readline().split())

dx=[0, 0, -1, 1]
dy=[-1, 1, 0, 0]
direction=['L', 'R', 'U', 'D']

x, y=1, 1
for i in cmd:
    for j in range(len(direction)):
        if i==direction[j]:
            new_x, new_y=x+dx[j], y+dy[j]
    if new_x>n or new_y>n or new_x<1 or new_y<1:
        continue
    x, y=new_x, new_y

print(x, y)