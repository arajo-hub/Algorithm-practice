import sys

# 수열의 길이 N, 연속합 조건 S 이상
N, S = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

# 0 ~ N까지의 합
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]  
    
answer = 1000001
start = 0
end = 1

while start != N:
    if sum_A[end] - sum_A[start] >= S:
        if end - start< answer:
            answer = end - start
        start += 1
        
    else:
        if end != N:
            end += 1
        else:
            start += 1

if answer != 1000001:
    print(answer)
else:
    print(0)