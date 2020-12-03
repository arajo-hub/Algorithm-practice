# import sys

# N, X=map(int, sys.stdin.readline().split())
# num=list(map(int, sys.stdin.readline().split()))

# cnt=0

# # 내 풀이
# def solution(list, X):
#     global cnt
#     idx=len(list)//2
#     left=list[:idx]
#     right=list[idx:]
#     if len(left)==1 and len(right)==1:
#         if X in left and X in right:
#             cnt+=2
#         elif X in left or X in right:
#             cnt+=1
#         else:
#             return -1
#     elif len(left)==1 and len(right)!=1:
#         if X in left:
#             cnt+=1
#         else:
#             solution(right, X)
#     elif len(left)!=1 and len(right)==1:
#         if X in right:
#             cnt+=1
#         else:
#             solution(left, X)
#     else:
#         solution(left, X)
#         solution(right, X)

#     if cnt==0:
#         return -1
#     else:
#         return cnt

# print(solution(num, X))

# # 첫 등장하는 인덱스와 마지막으로 등장하는 인덱스로 찾기

# def count_by_value(array, X):
#     N=len(array)
#     a=first(array, X, 0, N-1) # target의 첫 등장 위치를 찾고
#     if a==None:
#         return 0
#     b=last(array, X, 0, N-1) # target의 마지막 등장 위치를 찾아서
#     return b-a+1 # 개수를 구해준다.

# def first(array, target, start,end): # 앞에서부터 target이 첫 등장하는 인덱스를 찾아간다.
#     if start>end:
#         return None
#     mid=(start+end)//2 # 중간지점을 잡고
#     if (mid==0 or target>array[mid-1]) and array[mid]==target: # mid가 가장 왼쪽을 나타내거나 중간지점 직전값보다 target이 크고, array중간값이 target이라면
#         return mid # mid가 target이 첫 등장하는 인덱스가 된다.(정렬되어 있기 때문에 가능)
#     elif array[mid]>=target: # 중간값이 target보다 크다면(=중간값 왼쪽에 target이 있으면)
#         return first(array, target, start, mid-1) # end를 mid-1로 해서 다시 target의 첫 등장하는 위치를 찾는다.
#     else: # 중간값보다 target이 더 크다면(=중간값 오른쪽에 target이 있으면)
#         return first(array, target, mid+1, end) # start를 mid+1로 해서 다시 target의 첫 등장하는 위치를 찾는다.

# def last(array, target, start, end): # 앞에서부터 target이 마지막으로 등장하는 인덱스를 찾아간다.
#     if start>end:
#         return None
#     mid=(start+end)//2 # 중간지점을 잡고
#     if (mid==N-1 or target<array[mid+1]) and array[mid]==target: # mid가 가장 오른쪽을 나타내거나 중간지점 직후값보다 target이 작고, array중간값이 target이라면
#         return mid # mid가 target이 마지막으로 등장하는 인덱스가 된다.
#     elif array[mid]>target: # 중간값이 target보다 크다면(=중간값 인쪽에 target이 있으면)
#         return last(array, target, start, mid-1) # start를 mid-1로 해서 다시 target이 마지막으로 등장하는 위치를 찾는다.
#     else: # 중간값보다 target이 더 크다면
#         return last(array, target, mid+1, end) # start를 mid+1로 해서 다시 target이 마지막으로 등장하는 위치를 찾는다.

# count=count_by_value(num, X)

# if count==0:
#     print(-1)
# else:
#     print(count)

# 2020년 12월 3일

# 조건!!!
# 이 문제는 시간복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받음!!!

import sys

n, x=map(int, sys.stdin.readline().split())
nums=list(map(int, sys.stdin.readline().split()))

def getFirstIndex(array, target, start, end): # 배열 nums에서 x가 처음 등장하는 인덱스를 찾기 위한 함수
    if start>end:
        return None
    mid=(start+end)//2
    if (mid==0 or target>array[mid-1]) and array[mid]==target:
        return mid
    elif target<=array[mid]:
        return getFirstIndex(array, target, start, mid-1)
    else:
        return getFirstIndex(array, target, mid+1, end)

def getLastIndex(array, target, start, end): # 배열 nums에서 x가 마지막으로 등장하는 인덱스를 찾기 위한 함수
    if start>end:
        return None
    mid=(start+end)//2
    if (mid==n-1 or target<array[mid+1]) and array[mid]==target:
        return mid
    elif array[mid]>target:
        return getLastIndex(array, target, start, mid-1)
    else:
        return getLastIndex(array, target, mid+1, end)

def countValue(array, x):
    n=len(array)
    left=getFirstIndex(array, x, 0, n-1)
    if left==None:
        return 0
    right=getLastIndex(array, x, 0, n-1)
    return right-left+1

count=countValue(nums, x)

if count==0:
    print(-1)
else:
    print(count)

