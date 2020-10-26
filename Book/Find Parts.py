# import sys

# # 가장 단순한 방법

# N=int(sys.stdin.readline())
# parts=sorted(list(map(int, sys.stdin.readline().split())))

# M=int(sys.stdin.readline())
# customer=list(map(int, sys.stdin.readline().split()))

# for i in customer:
#     if i in parts:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 이진 탐색 알고리즘 이용하는 방법

# def binarySearch(array, target, start, end):
#     while start<=end:
#         mid=(start+end)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]>target:
#             end=mid-1
#         else:
#             start=mid+1
#     return None

# N=int(sys.stdin.readline())
# parts=sorted(list(map(int, sys.stdin.readline().split())))

# M=int(sys.stdin.readline())
# customer=list(map(int, sys.stdin.readline().split()))

# result=[]

# for i in customer:
#     result=binarySearch(parts, i, 0, N-1)
#     if result!=None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 계수 정렬을 이용하는 방법

# N=int(sys.stdin.readline())
# parts=[0]*1000000

# for i in map(int, sys.stdin.readline().split()):
#     parts[i]=1

# M=int(sys.stdin.readline())
# customer=list(map(int, sys.stdin.readline().split()))

# for i in customer:
#     if parts[i]==1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 2020년 10월 26일 풀이

import sys

n=int(sys.stdin.readline())

parts=list(map(int, sys.stdin.readline().split()))

m=int(sys.stdin.readline())

customer=list(map(int, sys.stdin.readline().split()))

parts.sort()

answer=[]
for i in range(m):
    if customer[i] in parts:
        answer.append("yes")
    else:
        answer.append("no")

print(*answer)