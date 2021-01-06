# 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence)
# 어떤 수열에서 일부 숫자를 지워서 만들 수 있는 증가하는 수열 중 제일 긴 수열

import sys

n=int(sys.stdin.readline()) # 수열의 크기
nums=list(map(int, sys.stdin.readline().split())) # 수열

dp=[0 for i in range(n)] # 수열과 같은 길이의 0으로 초기화된 배열

for i in range(len(nums)): # 숫자를 하나 꺼내서
    for j in range(i) : # 그 이전 숫자들과 비교를 해간다.
        if nums[i]>nums[j] and dp[i]<dp[j]: # 이전 수들의 길이 중 가장 긴 길이를 가져오는 것.
            dp[i]=dp[j]
    dp[i]+=1

print(max(dp))