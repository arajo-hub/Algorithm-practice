# 이 문제의 해결방법은 Counting Sort이다.
# Counting Sort는 나열된 수의 누적합을 이용해 정렬하는 방식이다.

import sys

case = int(input())
result = [0 for i in range(10001)] # 10001개짜리 리스트를 만들어준다. 이 문제 풀이법의 핵심. 잘못하다간 시간초과가 뜬다.

for num in sys.stdin:
    result[int(num)] += 1 # 입력하는 숫자를 result의 인덱스로 삼고, 그 자리에 1씩 올려 그 숫자가 등장하는 횟수를 저장한다.

for i in range(10001): # 위 리스트를 대상으로 for문을 돌리는데,
    if result[i] > 0: # result[i]가 0보다 크면(즉, 우리가 입력한 수의 나열에 등장하면)
        for j in range(result[i]): # 아까 1씩 올렸던 등장횟수만큼
            print(i) # print해준다.