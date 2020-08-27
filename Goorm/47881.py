import sys

N, K=map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))

answer=int(1e9)

start=nums.index(min(nums))

for i in range(K):
    cnt=1
    left, right=nums[:start-i], nums[start+K-i:]
    print(left, right)
    left_cnt=len(left)//(K-1)+(1 if len(left)%(K-1) else 0)
    right_cnt=len(right)//(K-1)+(1 if len(right)%(K-1) else 0)
    answer=min(answer, cnt+left_cnt+right_cnt)

print(answer)