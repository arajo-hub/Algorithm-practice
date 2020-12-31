# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수(경우의 수)를 구하는 프로그램을 작성하시오.

def isPossible(x): # x번째 열에 퀸을 놓을 수 있는지 아닌지 판별
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==x-i:
            return False
    return True

def dfs(x):
    global result
    if x==n:
        result+=1 # n개가 모두 들어갔다는 뜻
    else:
        for i in range(n):
            row[x]=i
            if isPossible(x):
                dfs(x+1)

import sys

n=int(sys.stdin.readline())

row=[0]*n
result=0
dfs(0)
print(result)