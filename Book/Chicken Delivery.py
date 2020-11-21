# from itertools import combinations
# import sys

# N, M=map(int, sys.stdin.readline().split())
# chicken, house=[], [] # 치킨집과 집을 각각의 리스트에 따로 저장

# for i in range(N):
#     data=(list(map(int, sys.stdin.readline().split()))) # 정보를 받아서
#     for j in range(N):
#         if data[j]==1: # 집(1)이라면
#             house.append((i, j)) # 좌표를 house에 넣고
#         elif data[j]==2: # 치킨집(2)이라면
#             chicken.append((i, j)) # 좌표를 chicken에 넣는다.

# candidates=list(combinations(chicken, M)) # combinations를 이용해 chicken 중 M개를 뽑는 경우의 수를 리스트로 만든다.

# def get_sum(candidate): # 합을 구하는 함수
#     result=0
#     for ax, ay in house: # 한 집을 기준으로
#         temp=1e9
#         for bx, by in candidate: # M개를 뽑는 한 조합의 그 집의 치킨거리 최소값을 구해 temp에 넣는다.
#             temp=min(temp, abs(ax-bx)+abs(ay-by))
#         result+=temp # result에 M개를 뽑아 최소의 합을 구한 temp를 더해준다.
#         print('result',result)
#     return result # 결국 result는 각 집의 최소 치킨거리의 합이 된다.

# result=1e9
# for candidate in candidates:
#     result=min(result, get_sum(candidate)) # 여러 개의 result 중에 최소값을 찾는다.

# print(result)

# 2020년 11월 21일 풀이

from itertools import combinations
import sys

n, m=map(int, sys.stdin.readline().split()) # 도시의 크기, 폐업시키지 않을 치킨집의 개수

chicken=[]
house=[]



for i in range(n): # 한 줄마다
    data=list(map(int, sys.stdin.readline().split())) # 정보를 받아서
    for j in range(n): # 각 위치마다 확인
        if data[j]==1: # 그집이 집(1)이라면
            house.append((i, j)) # 집만 모아놓은 리스트에 좌표를 넣는다.
        elif data[j]==2: # 집(1)이 아니고 치킨집(2)이라면
            chicken.append((i, j)) # 치킨집만 모아놓은 리스트에 좌표를 넣는다.

candidates=list(combinations(chicken, m)) # 치킨집들만 모아놓은 리스트에서 m개를 꺼내는 조합을 모두 만든다.

def get_sum(candidate):
    result=0
    for ax, ay in house: # 집에서 한 집의 좌표를 꺼내서
        temp=1e9
        for bx, by in candidate: # 치킨집 m개를 꺼내는 조합 중 한 개에서 치킨집 m개의 좌표를 꺼내가면서
            temp=min(temp, abs(ax-bx)+abs(ay-by)) # 최소 치킨거리를 계산해서
        result+=temp # result에 더한다.
    return result # 합계를 반환

result=1e9
for candidate in candidates: # 치킨집 m개를 꺼내는 조합들을 차례대로 조사해서
    result=min(result, get_sum(candidate)) # 최솟값을 찾는다.

print(result)