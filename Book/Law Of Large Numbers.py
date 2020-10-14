# 큰 수의 법칙

# import sys

# N, M, K=map(int, sys.stdin.readline().split())
# num=sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
# result=0

# while (1):

#     for i in range(K): # 한 index의 수는 최대 K번 더해질 수 있으므로 for문을 K번 돌린다.
#         if M==0: # M이 0이라면 반복문을 탈출한다.
#             break
#         result+=num[0] # 제일 큰 수(num[0])를 K번 더한다.(for문을 이용하여)
#         M-=1 # M은 반복문이 반복될 때마다 1씩 빼서 0이 되면 for문을 탈출할 수 있도록 한다.

#     if M==0: # M이 0이라면 while문을 탈출하는 조건이다.
#         break
#     result+=num[1] # M이 0이 아닐 때, 그 다음으로 큰 수를 더해준다.
#     M-=1 # 그리고 더해주는 횟수만큼 M을 줄여나간다.

# print(result)

# 2020년 10월 14일 풀이

import sys

n, m, k=map(int, sys.stdin.readline().split())
# n은 배열의 크기, m은 숫자가 더해지는 횟수, k는 더해질 수 있는 최대 횟수

num=list(map(int, sys.stdin.readline().split()))

num.sort(reverse=True)

result=0
while(True):
    for i in range(k):
        if m==0:
            break
        result+=num[0]
        m-=1
    if m==0:
        break
    result+=num[1]
    m-=1

print(result)