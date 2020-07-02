import sys

N, K=map(int, sys.stdin.readline().split())
# 물품의 수, 준서가 버틸 수 있는 무게

bag=[tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(bag)

knap=[0 for _ in range(K+1)]

print(knap)

for i in range(N):
    for j in range(K, 1, -1):
        if bag[i][0]<=j:
            knap[j]=max(knap[j], knap[j-bag[i][0]]+bag[i][1])

print(knap[-1])

# 코드 출처는 https://dojinkimm.github.io/problem_solving/2019/10/25/boj-12865-knapsack.html
# 해설은 https://dojinkimm.github.io/algorithm/2019/10/19/dp-2.html