import sys

n, c=map(int, sys.stdin.readline().split())

# n은 집의 개수, c는 공유기의 개수

home=[int(sys.stdin.readline()) for _ in range(n)]
home=sorted(home) # 집을 위치순으로 정렬
start, end = 1, home[-1]-home[0]
# 가장 인접한 두 공유기 사이의 거리는 1부터 첫집과 끝집 사이의 거리 안에 존재한다.
# 가장 인접한 두 공유기 사이의 거리가 가장 가까울 때는 1
# 가장 인접한 두 공유기 사이의 거리가 가장 멀 때는 첫집과 끝집 사이의 거리
# 이 거리를 조절해가면서 c개의 공유기가 모두 설치되면서 가장 인접한 두 공유기 사이의 거리가 최대가 되는 경우를 찾아간다.

def solution(distance):
    count=1 # 공유기 설치 수
    start=home[0] # 시작점은 제일 첫집으로 잡고
    for i in range(1, n): # 나머지 집들과 첫집을 비교
        if start+distance<=home[i]: # 첫집에서 후보거리만큼 떨어진 거리 이내에 있는 집이라면
            count+=1 # 공유기를 설치한다.
            start=home[i] # 그리고 시작집을 그 집으로 바꿔서 다음 집을 조시한다.
    return count

while start<=end:
    mid=(start+end)//2 # 최단거리와 최장거리의 중간(중간거리)으로 시작한다.

    if solution(mid)>=c: # 중간거리로 계산했을 때, c개보다 많은 공유기가 설치되거나, c개와 같은 공유기가 설치된다면
        answer=mid # 중간거리를 answer에 저장해두고,
        start=mid+1 # 시작점에 mid+1을 넣는다. 최대 거리를 구해야 하므로 계속 늘려서 c개보다 많거나 같은 개수의 공유기가 설치된다면 answer를 바꿔줘서 마지막에는 최대거리로 남게 된다.
    else: # 중간거리로 계산했을 때, c개보다 적은 수의 공유기가 설치된다면 중간거리를 줄여야 한다.
        end=mid-1

print(answer)