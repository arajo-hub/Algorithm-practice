import sys

S=sys.stdin.readline().strip('\n')

result=0
for num in S:
    if int(num)<=1 or result<=1:
        result+=int(num)
    else:
        result*=int(num)

print(result)