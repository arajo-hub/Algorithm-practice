import sys

N, M=map(int, sys.stdin.readline().split())

check=[0 for _ in range(N+1)] # 이미 사용했는지 체크
result=[0 for _ in range(M)]


def backtracking(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in range(1, n + 1):
        if check[i] == 1:  # 이미 사용했던 수라면 그냥 지나간다.
            continue
        result[index] = i  # 이미 사용하지 않은 수라면 continue에 걸리지 않으므로 result[index]에 값을 저장한다.
        for j in range(i + 1):
            check[j] = 1  # 들어간 숫자보다 작은숫자를 전부 체크한다.
        backtracking(index + 1, n, m)
        for j in range(1, n + 1):
            check[j] = 0  # 다음수로 넘어가기전에 전부 초기화한다.


backtracking(0, N, M)

# 아래는 백준사이트에서 본 다른 사람의 코드.

from itertools import combinations
# itertools.permutation을 이용하면 for문을 사용하지 않고도 순열을 구할 수 있고,
# itertools.combinations를 이용하면 조합을 구할 수 있다.

def n_and_m_2(N,M):


    L = combinations(range(1,N+1),M)

    for i in L:
        print(' '.join(map(str,i)))


N,M = input().split()
N,M = int(N), int(M)

n_and_m_2(N,M)