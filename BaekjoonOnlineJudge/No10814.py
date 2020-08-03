import sys

N=int(sys.stdin.readline())
member=[]

for i in range(N):
    age, name=sys.stdin.readline().split()
    member.append([int(age), i, name])

member=sorted(member)

for j in range(N):
    print(member[j][0], member[j][2])