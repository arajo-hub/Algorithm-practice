import sys

# 각각 가치가 다른 n개의 동전
# 합쳐서 k원 만들기
# 그 경우의 수
# 구성은 같은데 순서만 다르면 같은 경우

n, k=map(int, sys.stdin.readline().split())

coin=[]
dp=[0 for i in range(k+1)]
dp[0]=1

for _ in range(n):
    coin.append(int(sys.stdin.readline().strip('\n')))

for i in coin:
    for j in range(1, k+1):
        if j-i>=0:
            dp[j]+=dp[j-i]
            print(j, i)
print(dp[k])