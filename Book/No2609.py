import sys

x, y = map(int, sys.stdin.readline().split())

num1, num2 = x, y
while num2 != 0:
    num1 = num1 % num2
    num1, num2 = num2, num1
    print(num1, num2)

# 최대공약수
print(num1)

# 최대공배수
print(x*y//num1)