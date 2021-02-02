# 페르마의 소정리
# 어떤 수 p가 소수이고, a가 정수이면
# (a^(p-1))%p는 1이라는 것이다.
# 양변에 a^(-1)을 곱하면
# (a^(p-2))%p는 a^(-1)%p와 같다.

# 이 문제의 경우,
# (nCk)%1000000007을 구해야 한다.
# 풀어쓰면 (n!/(k!(n-k)!))%p이다.
# n!을 a, k!(n-k)!를 b라고 하면
# (a/b)%p이고,
# (a*b^(-1))%p
# (a%p)*(b^(-1)%p)
# (a*(b^(p-2)))%p // 페르마의 소정리에서 (b^(p-2))%p = b^(-1)%p
# 즉, b^(p-2)를 구해내기만 하면 문제를 해결할 수 있다.
# 정확히는 (n!*(k!(n-k)!)^(p-2))%p

import sys

n, k=map(int, sys.stdin.readline().split())

def solution(a, b):
    if(b % 2 > 0):
        return solution(a, b - 1) * a
    elif(b == 0):
        return 1
    elif(b == 1):
        return a
    else:
        result = solution(a, b//2)
        return result ** 2 % p

n_part = 1
nk_part = 1

p =  1000000007

# (n!*(k!(n-k)!)^(p-2))%p를 구해야 한다.

# n! 부분
for num in range(1, n+1):
    n_part *= num; n_part %= p

# k! 부분
for num in range(1, k+1):
    nk_part *= num; nk_part %= p

# (n-k)! 부분
for num in range(1, n-k+1):
    nk_part *= num; nk_part %= p
    
# (k!(n-k)!)^(p-2)
nk_part = solution(nk_part, p-2)%p

# (n!*(k!(n-k)!)^(p-2))%p
result = (n_part * nk_part) % p
print(result)

# 출처 : https://hon6036.github.io/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5/11401/