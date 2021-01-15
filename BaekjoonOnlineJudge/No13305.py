import sys

n=int(sys.stdin.readline()) # 도시의 개수

length=list(map(int, sys.stdin.readline().split())) # 인접한 두 도시를 연결하는 도로의 길이

price=list(map(int, sys.stdin.readline().split())) # 각 도시 주유소의 리터당 가격

result=[]
answer=0

result.append(length[0]*price[0])
standard=price[0] # 처음엔 기준가격을 첫 도시의 가격으로 잡는다.
for i in range(1, n-1):
    if price[i]<standard: # 기준가격이 현재 도시의 가격보다 높다면
        standard=price[i] # 기준가격을 바꿔주고
    result.append(standard*length[i]) # 기준가격으로 계산해서 넣는다.

print(sum(result))