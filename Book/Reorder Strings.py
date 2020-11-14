import sys

s=sys.stdin.readline().strip('\n')

result=[]
sum=0

for i in s:
    if i.isalpha():
        result.append(i)
    else:
        sum+=int(i)

result.sort()

if sum!=0:
    result.append(str(sum))

print(''.join(result))