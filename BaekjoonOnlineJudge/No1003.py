import sys

T=int(sys.stdin.readline())

# fibonacci(N)을 호출했을 때, fibonacci(0)과 fibonacci(1)이 몇번 호출되었는지 알기 위해
# 표를 그려보면, fibonacci(0)과 fibonacci(1)의 호출횟수또한 피보나치수열을 따르고 있다는 것을 알 수 있다.
# 그렇기 때문에 zero, one이라는 리스트(각 호출횟수만을 모아놓은 리스트)를 만들어서 피보나치 수열을 구하면 각각의 호출횟수를 알 수 있다.

def fibonacci(N):
    zero=[1, 0, 1] # 0의 호출횟수만 모아놓은 리스트
    one=[0, 1, 1] # 1의 호출횟수만 모아놓은 리스트
    length=len(zero) # 시작점을 나타낸다.
    if length<=N:
        for i in range(length, N+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    return [zero[N], one[N]]

for i in range(T):
    N=int(sys.stdin.readline())
    print(*fibonacci(N))