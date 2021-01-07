import sys

n=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
sums=[nums[0]]
for i in range(len(nums)-1):
    sums.append(max(sums[i]+nums[i+1], nums[i+1]))
    # sums에 nums의 첫 수를 넣고,
    # sums[i]에 nums[i+1]를 더한 값과
    # nums[i+1]을 비교해서 더 큰 값을 sums에 넣어준다.

print(max(sums))