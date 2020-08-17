# list를 이용한 풀이

import sys

students=[]

for i in range(int(sys.stdin.readline())):
    person=list(sys.stdin.readline().split())
    person[0], person[1]=int(person[1]), person[0]
    students.append(person)

students=sorted(students)

for j in students:
    print(j[1], end=' ')

# dictionary를 이용한 풀이

students={}

for i in range(int(sys.stdin.readline())):
    person=list(sys.stdin.readline().split())
    students[person[0]]=int(person[1])

for key, value in sorted(students.items(), key=lambda students:students[1]):
    print(key, end=' ')

# dictionary형에서 key를 기준으로 정렬하고 싶을 땐,
# sorted(dict.items(), key=lambda x:x[1]) (내림차순)
# sorted(dict.items(), reverse=True, key=lambda x:x[1]) (오름차순)