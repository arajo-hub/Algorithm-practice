import sys

N=int(sys.stdin.readline())
adventurer=list(map(int, sys.stdin.readline().split()))
team=[[] for i in range(N)]

team.sort()

count=0
result=0
for i in adventurer: # adventurer를 한명씩 꺼낸다.
    count+=1 # 팀원수를 센다.
    if count>=i: # 팀원수가 팀원의 공포와 같거나 크면
        result+=1 # 팀수를 1 올린다.
        count=0

print(result)