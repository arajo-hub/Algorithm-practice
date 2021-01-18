import math
import sys

# https://pacific-ocean.tistory.com/224 참고하여 작성했음.
# 주어진 숫자들이 오름차순이라고 가정하고,
# nums[0]=a*m+r
# nums[1]=b*m+r
# nums[2]=c*m+r
# m으로 나누어서 나머지(r)가 모두 같은 값이 나온다는 조건을 만족하려면 위의 상황과 같다.
# 이 상황에서 r을 제거하려면 nums[i]-nums[i-1]을 할 수 있다.
# a*m+r - (b*m+r) = a*m-b*m = m*(a-b)와 같다.
# 이 식이 모든 숫자들의 차마다 성립하므로, 숫자들의 차의 공약수를 구하면 그 값이 m이 된다.
# 이 문제의 시간 제한은 1초.
# 최대공약수만큼 for문을 돌리지 않고 최대공약수의 제곱근까지만 for문을 돌려주고 나머지는 계산.

n=int(sys.stdin.readline()) # 종이에 적은 수의 개수

nums=[]
result=[]
gcd=0

for i in range(n):
    nums.append(int(sys.stdin.readline())) # 입력받은 숫자를 리스트에 넣고
    if i==1: # 두 개째부터는 두 수의 차로 최대공약수를 구해준다.
        gcd=abs(nums[1]-nums[0])
    gcd=math.gcd(abs(nums[i]-nums[i-1]), gcd) # gcd : 최대공약수
gcd_a=int(gcd**0.5)

# for j in range(2, gcd_a+1):
#     if gcd%j==0:
#         result.append(j)
#         result.append(gcd//j)
# result.append(gcd)
# result=list(set(result))
# result.sort()

for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        result.append(i)
        result.append(gcd // i)
result.append(gcd)
result = list(set(result))
result.sort()

for k in result:
    print(k, end=" ")