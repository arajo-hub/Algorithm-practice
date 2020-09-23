def solution(num, start, end):
    if start>end:
        return None
    # 중간점을 잡아서 left, right 리스트로 나누고 어느 쪽을 탐색할 것인지 정한다.
    mid=(start+end)//2
    if num[mid]==mid: # 중간점이 고정점이라면 반환
        return mid
    elif num[mid]>mid: # 중간점의 값이 index보다 크다면 중간점 기준으로 왼쪽만 탐색하면 되므로
        return solution(num, start, mid-1) # 왼쪽(start부터 mid-1까지)을 탐색한다.
    elif num[mid]<mid: # 중간점의 값이 index보다 작다면 중간점 기준으로 오른쪽만 탐색하면 되므로
        return solution(num, mid+1, end) # 오른쪽(mid+1부터 end까지)을 탐색한다.

import sys

N=int(sys.stdin.readline())
num=list(map(int, sys.stdin.readline().split()))

result=solution(num, 0, N-1)

if result:
    print(result)
else:
    print(-1)