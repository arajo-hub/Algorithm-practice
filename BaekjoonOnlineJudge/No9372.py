import sys

t = int(sys.stdin.readline())

for _ in range(t):
    # 국가의 수 n, 비행기의 종류 m
    n, m = map(int, sys.stdin.readline().split())

    for _ in range(m):
        # a와 b를 왕복하는 비행기가 있음.
        a, b = map(int, sys.stdin.readline().split())
    
    # 주어지는 비행 스케줄은 항상 연결 그래프를 이룬다.
    # -> 모든 국가가 연결되어 있다!
    # 첫번째에서 두번째, 두번째에서 세번째, ... , n-1번째에서 n번째까지 비행기는 n-1이 최소!
    print(n-1)