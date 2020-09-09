from itertools import combinations
import sys

N, M=map(int, sys.stdin.readline().split())
chicken, house=[], [] # 치킨집과 집을 각각의 리스트에 따로 저장

for i in range(N):
    data=(list(map(int, sys.stdin.readline().split()))) # 정보를 받아서
    for j in range(N):
        if data[j]==1: # 집(1)이라면
            house.append((i, j)) # 좌표를 house에 넣고
        elif data[j]==2: # 치킨집(2)이라면
            chicken.append((i, j)) # 좌표를 chicken에 넣는다.

candidates=list(combinations(chicken, M)) # combinations를 이용해 chicken 중 M개를 뽑는 경우의 수를 리스트로 만든다.

def get_sum(candidate): # 합을 구하는 함수
    result=0
    for ax, ay in house: # 한 집을 기준으로
        temp=1e9
        for bx, by in candidate: # M개를 뽑는 한 조합의 그 집의 치킨거리 최소값을 구해 temp에 넣는다.
            temp=min(temp, abs(ax-bx)+abs(ay-by))
        result+=temp # result에 M개를 뽑아 최소의 합을 구한 temp를 더해준다.
        print('result',result)
    return result # 결국 result는 각 집의 최소 치킨거리의 합이 된다.

result=1e9
for candidate in candidates:
    result=min(result, get_sum(candidate)) # 여러 개의 result 중에 최소값을 찾는다.

print(result)