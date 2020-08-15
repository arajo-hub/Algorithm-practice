import sys

N, M=map(int, sys.stdin.readline().split())
maze=[list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(N)]

for _ in range(len(maze)):
    print(maze[_])

cnt=1

# 이동방법은 두 가지
# 오른쪽으로 가거나(x는 +1, y는 0)
# 아래쪽으로 가거나(x는 0, y는 +1)

def dfs(x, y):
    for i in range(N):
        for j in range(M):
            if maze[x][y]==1:
                global cnt
                cnt+=1
                new_x, new_y=x, y
                dfs(new_x, new_y)
                return True
            else:
                return False

for i in range(N):
    for j in range(M):
        if dfs(0, 0)==True:
            cnt+=1

print(cnt)