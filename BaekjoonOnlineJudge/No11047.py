# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

import sys

n, k=map(int, sys.stdin.readline().split()) # 동전의 갯수, 만들고자 하는 금액

coin=[int(sys.stdin.readline()) for _ in range(n)] # 동전의 가치

result=0
for i in range(n-1, -1, -1):
    if (k//coin[i])<1: # 그 동전으로 할 수 없다면
        continue # 다음 동전으로 넘긴다.
    else: # 그 동전으로 할 수 있다면
        result+=k//coin[i] # 몫은 result에 넣고.
        k%=coin[i] # 나머지는 앞으로 동전으로 나눠야 한다.

print(result)