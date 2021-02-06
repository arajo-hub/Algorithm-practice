# 행렬과 피보나치 수
# 피보나치 수의 점화식
# F(n)=F(n-1)+F(n-2) : n-1 위치의 수와 n-2 위치의 수를 더하면 n 위치의 수가 된다.
# 행렬로 바꿔보면
# (F(n)  )  =   (1 1) * (F(n-1))
# (F(n-1))      (1 0)   (F(n-2))
# 이때, 오른쪽 변의 피보나치수가 들어간 행렬도 같은 방식으로 바꿀 수 있으므로
# 결과적으로 아래와 같아진다.
# (F(n)  )  =   (1 1)^(n-1) * (F(1)) -> F(1)은 1
# (F(n-1))      (1 0)         (F(0)) -> F(0)은 0
# (F(n)  )  =   (1 1)^(n-1) * (1)
# (F(n-1))      (1 0)         (0)

# 내 풀이 -> 시간 초과!

# import sys

# n=int(sys.stdin.readline())

# # (1 1)
# # (1 0) 행렬을 n번 곱하기

# a=[[1, 1], [1, 0]]

# def multiple(a, n):

#     if n==1:
#         return a
#     else:
#         if n%2==0:
#             temp=[[0, 0], [0, 0]]
#             c=multiple(a, n//2)
        
#             for i in range(2):
#                 for j in range(2):
#                     for t in range(2):
#                         temp[i][j] += c[i][t] * c[t][j]
#             return temp
#         else:
#             temp=[[0, 0], [0, 0]]
#             c=multiple(a, n-1)

#             for i in range(2):
#                 for j in range(2):
#                     for t in range(2):
#                         temp[i][j] += c[i][t] * a[t][j]
#             return temp

# print(multiple(a, n-1)[0][0]%1000000007)

# 다른 풀이

#2^x 피보나치를 구해주는 함수
def matrix_mul_self(x):
    base = [[1, 1], [1, 0]]
    result = [[1, 1], [1, 0]]
    for _ in range(x):
        result = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    result[i][j] += (base[i][k] * base[k][j]) % 1000000007
        base = result
        
    return result

#2*2 두 행렬의 곱을 구해주는 함수
def matrix_mul(a, b):
    result = [[0 ,0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += (a[i][k] * b[k][j]) % 1000000007
                
    return result

import sys

n = bin(int(sys.stdin.readline()))[2:] # 입력받을 수를 2진수로 바꾼다.
# def bin(number: Union[int, _SupportsIndex])
# Return the binary representation of an integer.
# bin(2796202) '0b1010101010101010101010'
# 모든 자연수는 2의 제곱수의 합으로 표현할 수 있다.
# 2^1을 제곱하고, 그 결과를 제곱, 또 그 결과물을 제곱... 그렇게 해서 원하는 수를 찾을 수 있다.

result = [[1, 0], [0, 1]]

for i in range(len(n)):
    if n[-i-1] == '1': #2^x 피보나치 행렬들만 구해서 그 행렬들끼리 곱한다.
        result = matrix_mul(result, matrix_mul_self(i))
        
print(result[0][1] % 1000000007)

# 출처 : https://claude-u.tistory.com/406