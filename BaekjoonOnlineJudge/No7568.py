# 내 풀이

# import sys

# n=int(sys.stdin.readline()) # 사람 수

# people=[]
# for i in range(n):
#     x, y=map(int, sys.stdin.readline().split()) # 몸무게와 키
#     people.append((x, y, i))

# people.sort(key=lambda x:(-x[0], x[1]))

# rank=1
# result=[]
# for j in range(len(people)):
#     for k in range(len(people)):
#         if people[j][0]<people[k][0] and people[j][1]<people[k][1]:
#             rank+=1
#     result.append((rank, people[j][2]))
#     rank=1

# result.sort(key=lambda x:x[1])

# for h in result:
#     print(h[0], end=" ")

# 보완한 풀이

import sys

n=int(sys.stdin.readline())
w=[]
h=[]

for _ in range(n):
    x, y=map(int, sys.stdin.readline().split())
    w.append(x)
    h.append(y)

for i in range(len(w)):
    count=1
    for j in range(len(w)):
        if w[i]<w[j] and h[i]<h[j]:
            count+=1
    print(count, end=" ")