# import sys

# N=int(sys.stdin.readline())
# grade=[]

# for i in range(N):
#     name, l, e, m=sys.stdin.readline().split()
#     l, e, m=int(l), int(e), int(m)
#     grade.append((l, e, m, name))

# grade.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))
# # 이 코드는 기억해둘 것. -는 내림차순.
# # 국어(x[0]) 점수가 감소하는 순서로,
# # 국어 점수가 같으면 영어 점수(x[1])가 증가하는 순서로,
# # 국어 점수와 영어 점수가 같으면 수학 점수(x[2])가 감소하는 순서로,
# # 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로(대문자가 소문자보다 앞)

# for each in grade:
#     print(each[-1])

# 2020년 11월 29일 풀이

import sys

n=int(sys.stdin.readline())
students=[]

for i in range(n):
    name, l, e, m=sys.stdin.readline().split()
    l, e, m=int(l), int(e), int(m)
    students.append((l, e, m, name))

students.sort(key=lambda x:(-x[0], x[1], -x[2], x[3]))

for i in students:
    print(i[-1])