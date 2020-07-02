import sys

N, K=map(int, sys.stdin.readline().split())
# 물품의 수, 준서가 버틸 수 있는 무게

weight=[]
value=[]

for i in range(N):
    W, V=map(int, sys.stdin.readline().split())
    weight.append([W, V])

print(sorted(weight))