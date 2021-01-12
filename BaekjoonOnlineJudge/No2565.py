import sys

n=int(sys.stdin.readline()) # 전깃줄의 개수

elec = [] # A전봇대와 B전봇대의 전깃줄 연결 정보
only_b = [] # B전봇대의 연결 정보만 저장하는 배열
dp = [0 for i in range(n)]

for i in range(n): # 전깃줄 연결 정보를 저장한다.
    elec.append(list(map(int, sys.stdin.readline().split())))

elec.sort(key = lambda x:x[0]) # A전봇대 기준으로 정렬

for i in range(n):
    only_b.append(elec[i][1]) # B전봇대의 연결 정보만 저장한다.

# LIS
for i in range(n):
    for j in range(i):
        if only_b[i] > only_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))