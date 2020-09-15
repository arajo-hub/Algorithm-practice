import sys

N=int(sys.stdin.readline()) # 수의 개수
nums=list(map(int, sys.stdin.readline().split())) # 수들을 입력한다.
add, sub, mul, div=map(int, sys.stdin.readline().split()) # 연산자의 개수 입력

min_value=1e9
max_value=-1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i==N: # 전체 수를 모두 보았다면
        min_value=min(min_value, now) # min_value의 최소값,
        max_value=max(max_value, now) # max_value의 최대값 결정
    else: # 아직 진행중이면 연산 진행
        if add>0:
            add-=1
            dfs(i+1, now+nums[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1, now-nums[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1, now*nums[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1, int(now/nums[i]))
            div+=1

dfs(1, nums[0])

print(max_value)
print(min_value)