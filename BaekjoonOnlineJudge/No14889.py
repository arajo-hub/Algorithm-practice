# 1부터 차례대로 넣으면서 대조.
# choice=list(permutations(card, 3))
from itertools import combinations
import sys

n=int(sys.stdin.readline())
person=[j+1 for j in range(n)]
choice=list(combinations(person, len(person)//2)) # 팀을 나누는 모든 경우의 수

ability=[]
for i in range(n):
    ability.append(list(map(int, sys.stdin.readline().split())))

result=[]

def get_total(array):
    total=0
    for x, y in combinations(array, 2):
        total+=ability[x-1][y-1]+ability[y-1][x-1]
    return total

for s in choice: # 팀을 나누는 모든 경우의 수에서 능력치를 계산한다.
    start, link=0, 0
    team_link=[]
    start=get_total(s)
    for k in person:
        if k not in s: # 팀으로 안 뽑힌 사람들을 꺼내어
            team_link.append(k) # 따로 팀을 만들고
        else:
            continue
    link=get_total(team_link)
    result.append(abs(start-link))

print(min(result))