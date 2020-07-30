# 이 문제의 중요포인트는 테스트케이스 숫자 N은 가장 작은 차를 가진 두 소수의 합이라는 것이다.
# N을 2로 나눈 수(n)에서 출발하여 발견하는 소수(a)마다 N-a가 소수인지 판별한 후 소수라면 return해주면 된다.
# n이 0이 될 때까지 반복할 필요가 없는 이유는 a와 N-a가 둘 다 소수인 경우를 제일 처음 찾았을 때의 경우가 차가 가장 작기 때문이다.

# 간단히 말하자면,
# 1단계 : N을 2로 나누고(n)
# 2단계 : n에서 -1을 해가며 소수인지 판별한다. (시작점은 n부터. n이 소수인지 판별한 후, 소수가 아니라면 -1)
# 3단계 : -1을 한 수가 소수인지 판별한 후, 맞다면 return. 소수가 아니라면 n에 -1.

def primenumber(n):
    for i in range(2, n-1):
        if n%i==0:
            return False
    return True

def solution(N):
    n=N//2
    while(n!=0):
        if primenumber(n):
            if primenumber(N-n):
                return [n, N-n]
            else:
                n-=1
        else:
            n-=1

for i in range(int(input())):
    N=int(input())
    print(*solution(N))