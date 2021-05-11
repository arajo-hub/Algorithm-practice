import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

decimal = []

for i in range(m, n+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
            if count > 2:
                break
    if count == 2:
        decimal.append(i)

if len(decimal) != 0:
    print(sum(decimal))
    print(decimal[0])
else:
    print('-1')