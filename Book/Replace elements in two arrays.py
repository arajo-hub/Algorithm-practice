import sys

N, K=map(int, sys.stdin.readline().split())

array1=sorted(list(map(int, sys.stdin.readline().split())))
array2=sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

for i in range(K):
    if array1[i]<array2[i]:
        array1[i], array2[i]=array2[i], array1[i]
    else:
        break

print(sum(array1))