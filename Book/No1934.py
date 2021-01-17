import sys

tc=int(sys.stdin.readline())

for test in range(tc):
    x, y = map(int, sys.stdin.readline().split())

    num1, num2 = x, y
    while num2 != 0:
        num1 = num1 % num2
        num1, num2 = num2, num1

    # 최소공배수
    print(x*y//num1)