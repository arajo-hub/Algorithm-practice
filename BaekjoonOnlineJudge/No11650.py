import sys

point=[]

for i in range(int(sys.stdin.readline())):
    x, y=map(int, sys.stdin.readline().split())
    point.append([x, y])

point=sorted(point)

for j in range(len(point)):
    print(*point[j])