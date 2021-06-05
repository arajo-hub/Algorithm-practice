# TSP
# Traveling Salesman Problem
# Computer Science 분야에서 가장 중요하게 취급되는 문제 중 하나

# 1번부터 N번까지 번호가 매겨져 있는 도시.
# 도시들 사이에는 길이 있다. (없을 수도)
# 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐
# 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
# 단, 한 번 갔던 도시로는 다시 갈 수 없다.
# 가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

import sys

def solution(N, W, dp):
    for i in range(N):
        for j in range(N):
            if not W[i][j]: # 비용이 0이 아닌 경우
                W[i][j] = float('INF')
    
    for i in range(1, N):
        dp[i][0] = W[i][0]

    for k in range(1, N-1):
        for route in range(1, size):
            if count(route, N) == k:
                for i in range(1, N):
                    if not isIn(i, route):
                        dp[i][route] = get_minimum(N, W, i, route, dp)
    
    dp[0][size - 1] = get_minimum(N, W, 0, size - 1, dp)

    return dp[0][size - 1]

def count(route, N):
    cnt = 0
    for n in range(1, N):
        if route & (1 << n - 1) != 0:
            cnt += 1
    return cnt

def isIn(i, route):
    if route & (1 << i - 1) != 0:
        return True
    else:
        return False
    
def get_minimum(N, W, i, route, dp):
    minimum_dist = float('INF')
    for j in range(1, N):
        if isIn(j, route):
            before_route = route & ~(1 << j - 1) # 비트연산을 이용한 조건문
            dist = W[i][j] + dp[j][before_route]
            if minimum_dist > dist:
                minimum_dist = dist
    return minimum_dist

N = map(int, sys.stdin.readline().split())

W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

size = 2 ** (N - 1)

dp = [[float('INF')] * size for _ in range(N)]

print(solution(N, W, dp))

# 출처 : https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-2098-%EC%99%B8%ED%8C%90%EC%9B%90%EC%88%9C%ED%9A%8C-Python