import sys

n, m = map(int, sys.stdin.readline().split())

maze = []
queue = []

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    maze.append(list(input()))

queue = [[0, 0]]
maze[0][0] = 1

while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and maze[x][y] == "1":
            queue.append([x, y])
            maze[x][y] = maze[a][b]+1

print(maze[n-1][m-1])