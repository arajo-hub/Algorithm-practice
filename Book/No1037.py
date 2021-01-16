import sys

count=int(sys.stdin.readline()) # 진짜 약수의 개수
nums=list(map(int, sys.stdin.readline().split()))
nums.sort()

print(nums[0]*nums[-1])