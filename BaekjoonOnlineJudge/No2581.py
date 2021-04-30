import sys

# m 이상 n 이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 구하는 문제

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

decimal_list = []
 
# 숫자를 하나씩 바꿔가며
for i in range(m, n+1):
    count = 0
    # 그 숫자를 나눌 숫자를 하나씩 꺼낸다.
    for j in range(1, i+1):
        if i % j == 0: # 나눠지면
            count += 1 # count를 올려주고.
            if count > 2: # count가 2보다 커지면 소수라고 볼 수 없음.
                break

    if count == 2: # 소수라면

        decimal_list.append(i) # 리스트에 넣고

if len(decimal_list) != 0: # 소수가 하나라도 있다면
    print(sum(decimal_list)) # 소수들의 합을 출력한다.
    print(decimal_list[0]) # 최솟값을 출력
else: # 소수가 없다면
    print('-1') # -1을 출력