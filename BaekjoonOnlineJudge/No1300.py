from math import pow
import sys

n=int(sys.stdin.readline()) # 배열의 크기
k=int(sys.stdin.readline()) # 배열의 크기

# 2차원 배열을 1차원으로 풀었을 때의 문제이다.
# 어떤 수 x가 오름차순으로 몇 번째인지 구하고 싶다면,
# 배열에서 x보다 작거나 같은 수가 몇 개 있는지 구하면 된다.
# 예를 들어 x가 20이라고 하면
# 1일 때, 1*1~1*10 (10개)
# 2일 때, 2*1~2*10 (10개)
# 3일 때, 3*1~3*6 (6개)
# 4일 때, 4*1~4*5 (5개)
# ... 이런식으로 나가게 된다.
# 규칙을 찾아보면 20을 행으로 나눈 몫이 개수가 된다는 걸 알 수 있다.

start, end=1, k

while start<=end:
    mid=(start+end)//2
    result=0

    for i in range(1, n+1):
        result+=min(mid//i, n)
    
    if result>=k:
        answer=mid
        end=mid-1
    else:
        start=mid+1

print(answer)

# 출처 : https://claude-u.tistory.com/449