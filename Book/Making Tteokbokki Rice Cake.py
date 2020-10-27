# import sys

# N, M=map(int, sys.stdin.readline().split())

# tteok=list(map(int, sys.stdin.readline().split()))

# # 원하는 길이만큼 떡을 남기기 위한 적정한 절단기 높이는
# # 0과 가장 긴 떡의 길이 사이에 있다.
# # (가장 긴 떡보다 절단기 높이가 길면 자르는 의미가 없다. 나머지 떡이 생기지 않기 때문에.)

# start=0
# end=max(tteok)
# result=0

# while(start<=end):
#     total=0
#     mid=(start+end)//2 # 중간값을 정하고,
#     for i in tteok:
#         if i>mid: # 중간값보다 긴 떡이라면
#             total+=(i-mid) # 중간값을 뺀 떡 길이(=절단기로 자르고 난 나머지 떡의 길이)를 total에 더해준다.
#     if total<M: # 원하는 나머지 떡의 길이보다 total이 작다면
#         end=mid-1 # 가장 긴 떡의 길이에서 -1을 한다.
#     else: # total이 원하는 나머지 떡의 길이보다 같거나 크다면
#         result=mid # 그 중간값(=절단기 높이)을 result에 저장하고
#         start=mid+1 # 시작점에 +1을 한다.

# print(result)

# 2020년 10월 27일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())
tteok=list(map(int, sys.stdin.readline().split()))

start=0
end=max(tteok)
result=0

while(start<=end):
    total=0
    mid=(start+end)//2
    for i in tteok:
        if i>mid:
            total+=i-mid
    if total>=m:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)