import sys

N, C=map(int, sys.stdin.readline().split())
distance=[]

for i in range(N):
    temp=int(sys.stdin.readline())
    distance.append(temp)
distance.sort()

start=distance[1]-distance[0] # 집 사이의 거리 중 가장 작은 값(=첫번째집과 두번째집의 거리)
end=distance[-1]-distance[0] # 집 사이의 거리 중 가장 큰 값(=첫번째집과 마지막집의 거리)
result=0

while(start<=end):
    mid=(start+end)//2 # 가장 가까운 거리와 가장 먼 거리의 중간값을 저장한다.
    value=distance[0]
    count=1
    for i in range(1, N):
        if distance[i]>=value+mid: # 첫 집에 거리의 중간값을 더한 값보다 멀리 있는 집이라면
            value=distance[i] # 기준을 그집으로 바꿔주고,
            count+=1
    if count>=C: # C개 이상의 공유기를 설치할 수 있다면 거리를 늘리고
        start=mid+1
        result=mid
    else: # 설치할 수 없다면 길이를 줄인다.
        end=mid-1

print(result)