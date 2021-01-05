# 메모이제이션(Memoization)
# 동일한 계산을 반복해야 할 경우 한 번 계산한 결과를 메모리에 저장해두었다가 꺼내씀으로써 중복 계산을 방지할 수 있게 하는 기법
# 동적계획법의 핵심이 되는 기술

import sys

dp=[[[0]*21 for _ in range(21)] for _ in range(21)]
# 함수 w의 결과를 저장할 배열
# 각 수가 20을 넘으면 20으로 w에 넣기 때문에 편의상 21칸으로 해야 한다.

def w(a, b, c):

    # 1. 세 수 중 한 수라도 0보다 작거나 같을 때
    if a<=0 or b<=0 or c<=0:
        return 1
    # 2. 세 수 중 한 수라도 20보다 클 때
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    # dp는 0으로 초기화되기 때문에
    # dp[a][b][c]가 0이 아닌 어떤 값이라면
    # dp[a][b][c]의 결과가 저장된 것이다.
    # 즉, 결과가 이미 존재한다면 그 결과를 return 한다.
    if dp[a][b][c]:
        return dp[a][b][c]

    # 3. a < b < c의 관계를 가지고 있을 때
    if a<b<c:
        dp[a][b][c]=w(a, b, c-1)+w(a, b-1, c-1)-w(a, b-1, c)
        return dp[a][b][c]
    
    # 1, 2, 3의 경우에 속하지 않을 때
    dp[a][b][c]=w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

while True:
    a, b, c=map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    print("w(%d, %d, %d) = %d"%(a, b, c, w(a, b, c)))