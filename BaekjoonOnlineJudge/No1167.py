import sys

v = int(sys.stdin.readline())

matrix =[[] for _ in range(v+1)]

for _ in range(v):
    # 정점(A)번호, 그 정점(A)과 연결된 정점(B)번호, 그 정점(B)까지의 거리
    info = list(map(int, sys.stdin.readline().split()))

    info_length = len(info)

    for i in range(1, info_length//2):
        matrix[info[0]].append([info[2*i-1], info[2*i]])

# 첫번째 dfs 결과
dfs_result = [0 for _ in range(v+1)]

def dfs(start, matrix, result):
    for i, j in matrix[start]:
        if result[i]==0:
            result[i] = result[start]+j
            dfs(i, matrix, result)

dfs(1, matrix, dfs_result)
dfs_result[1] = 0

max_value = 0
index = 0

for i in range(len(dfs_result)):
    if max_value<dfs_result[i]:
        max_value = dfs_result[i]
        index = i

dfs_again_result = [0 for _ in range(v+1)]
dfs(index, matrix, dfs_again_result)
dfs_again_result[index] = 0
print(max(dfs_again_result))