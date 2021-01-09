# import sys

# N, K=map(int, sys.stdin.readline().split())
# # 물품의 수, 준서가 버틸 수 있는 무게

# bag=[tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# print(bag)

# result=[0 for _ in range(K+1)]

# print(result)

# for i in range(N):
#     for j in range(K, 1, -1):
#         if bag[i][0]<=j:
#             result[j]=max(result[j], result[j-bag[i][0]]+bag[i][1])

# print(result[-1])

# # 코드 출처는 https://dojinkimm.github.io/problem_solving/2019/10/25/boj-12865-resultsack.html
# # 해설은 https://dojinkimm.github.io/algorithm/2019/10/19/dp-2.html

# 2021년 1월 8일 풀이

import sys

n, k=map(int,sys.stdin.readline().split()) # 물품의 수와 준서가 버틸 수 있는 무게

bag=[]

for i in range(n):
    w, v=map(int,sys.stdin.readline().split()) # 물건의 무게와 가치
    bag.append((w, v))

result=[0 for _ in range(k+1)] # 각 무게마다 칸이 있는 배열

for j in range(n):
    for t in range(k, 1, -1):
        if bag[j][0]<=t:
            result[t]=max(result[t], result[t-bag[j][0]]+bag[j][1])

print(result[-1])