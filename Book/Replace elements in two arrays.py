# import sys

# N, K=map(int, sys.stdin.readline().split())

# array1=sorted(list(map(int, sys.stdin.readline().split())))
# array2=sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

# for i in range(K):
#     if array1[i]<array2[i]:
#         array1[i], array2[i]=array2[i], array1[i]
#     else:
#         break

# print(sum(array1))

# 2020년 10월 25일 풀이

import sys

n, k=map(int, sys.stdin.readline().split())

arrayA=list(map(int, sys.stdin.readline().split()))
arrayB=list(map(int, sys.stdin.readline().split()))

arrayA.sort()
arrayB.sort(reverse=True)

for i in range(k):
    if arrayA[i]<arrayB[i]:
        arrayA[i], arrayB[i]=arrayB[i],arrayA[i]
    else:
        break

print(sum(arrayA))