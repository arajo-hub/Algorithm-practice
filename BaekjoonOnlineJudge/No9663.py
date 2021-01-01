# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수(경우의 수)를 구하는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline())

def dfs(arr):
    global ans
    length = len(arr)
    if length==n:
        ans+=1
        return
    candidate = list(range(n)) # 후보가 될 수 있는 자리를 0부터 n-1까지 만들고 제외하는 방법을 사용
    for i in range(length):
        if arr[i] in candidate:  # 같은 가로줄에 있으면 후보에서 제외
            candidate.remove(arr[i])
        distance = length - i
        if arr[i] + distance in candidate:  # 같은 '/' 대각선에 있으면 후보에서 제외
            candidate.remove(arr[i] + distance)
        if arr[i] - distance in candidate:  # 같은 '\' 대각선에 있으면 후보에서 제외
            candidate.remove(arr[i] - distance)
    if candidate:
        for i in candidate:
            arr.append(i)
            dfs(arr)
            arr.pop()
    else:
        return

ans = 0
for i in range(n):
    dfs([i])
print(ans)