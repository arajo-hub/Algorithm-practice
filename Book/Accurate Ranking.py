# import sys

# INF=int(1e9)

# n, m=map(int, sys.stdin.readline().split())

# graph=[[INF]*(n+1) for _ in range(n+1)]

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a==b:
#             graph[a][b]=0 # 같은 번호의 학생은 동일인물이므로 0

# for _ in range(m):
#     a, b=map(int, sys.stdin.readline().split()) # a번 학생이 b번 학생보다 성적이 낮다는 의미를 가지고 있다.
#     graph[a][b]=1

# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
#             # a에서 b로 도달하는 방법은 a에서 b로 가는 경로와 a에서 k로 갔다가 k에서 b로 가는 경로 중 비용이 적은 경로를 선택한다.

# result=0

# # 학생을 한명씩 확인하며 도달 가능한지 체크
# for i in range(1, n+1):
#     count=0
#     for j in range(1, n+1):
#         if graph[i][j]!=INF or graph[j][i]!=INF: # INF일 경우는 도달 불가능하다는 의미이다.
#             count+=1
#         if count==n: # 정확한 순위를 알 수 있는 경우를 출력하는 것이므로 count가 n과 같을 경우만 result에 +1을 해준다.
#             result+=1

# print(result)

# 2020년 12월 15일 풀이

import sys

n, m=map(int, sys.stdin.readline().split()) # n은 학생들의 수, m은 두 학생의 성적을 비교한 횟수

INF=1e9

array=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==j:
            array[i][j]=0

for _ in range(m):
    a, b=map(int, sys.stdin.readline().split())
    array[a][b]=1

for k in range(1, n+1):
    for h in range(1, n+1):
        for l in range(1, n+1):
            array[h][l]=min(array[h][l], array[h][k]+array[k][l])

result=0

for t in range(1, n+1):
    count=0
    for g in range(1, n+1):
        if array[t][g]!=INF or array[g][t]!=INF:
            count+=1
        if count==n:
            result+=1

print(result)