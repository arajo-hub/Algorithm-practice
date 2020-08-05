# 예제 3-1 거스름돈

# 주석으로 표시된 코드는 내가 작성했지만 책을 참고하여 수정해야 할 부분이다.

import sys

N=int(sys.stdin.readline())
coin=[500, 100, 50, 10]
count=0
# count=[0, 0, 0, 0] list를 설정해주는 것보다 count를 int로 선언해서 단순히 더하는 게 더 간단하다.

for i in range(len(coin)):
    count+=N//coin[i]
    N%=coin[i]
    # N-=coin[i]*(N//coin[i])

print(count)
# print(sum(count))