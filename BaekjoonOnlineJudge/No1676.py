import sys
from math import factorial

# 1. 내 풀이
# factorial을 이용해서 팩토리얼 결과를 얻고,
# 10으로 나눠가면서 0의 개수를 센다.

# n=int(sys.stdin.readline())

# count=0
# num=factorial(n)

# while (True):
#     if num%10==0:
#         num//=10
#         count+=1
#     else:
#         break

# print(count)

# 2. 간단한 풀이
# 어떤 n 팩토리얼의 값에 끝자리부터 0이 몇 개인지 알고 싶다면 10이 몇 개인지 알면 된다.
# 그런데 10은 2와 5의 곱, 2는 충분히 많기 때문에(짝수이기만 하면 되니까) 5의 개수를 알면
# 0의 개수를 알 수 있다.
# 이때, 5의 개수는 n//5로 구할 수 있고,
# 25와 125 같은 5의 제곱수이므로
# n//5에 n//25를 더해주고 n//125를 더해준다.
# n의 범위가 0부터 500까지로 설정되어 있기 때문에 n//125까지 더해준다.
 
n=int(sys.stdin.readline())
print(n//5 + n//25 + n//125)