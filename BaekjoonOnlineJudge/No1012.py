from sys import stdin
read=stdin.readline

for i in range(int(read())):
    garo, sero, cnt=map(int, read().split())
    matrix=[[0]*(garo) for i in range(sero)]

# for _ in range(cnt):
#     link = list(map(int, read().split()))
#     matrix[link[0]][link[1]] = 1

for j in range(len(matrix)):
    print(matrix[j])