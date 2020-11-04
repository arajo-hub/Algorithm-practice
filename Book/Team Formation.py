# import sys

# def teamup(parent, a, b):
#     a=checkteam(parent, a) # a와
#     b=checkteam(parent, b) # b가 들어있는 팀을 찾아서
#     if a<b: # a보다 b가 크다면
#         parent[b]=a # 더 큰 숫자인 b의 팀을 a로 바꾼다.
#     else: # b가 a보다 크거나 같다면
#         parent[a]=b # 더 큰 숫자인 a의 팀을 b로 바꾼다.

# def checkteam(parent, num): # 어떤 숫자 num이 어떤 팀에 들어있는지 확인한다.
#     if parent[num]!=num: # num의 팀이 'num'이 아니라면
#         parent[num]=checkteam(parent, parent[num]) # 그 팀은 어느 팀인지 찾는다.
#     return parent[num]

# N, M=map(int, sys.stdin.readline().split())

# # team을 나타내는 list를 만든다.
# # 이 team 리스트를 간단히 설명해보자면,
# # [0, 1, 2, ... , N]
# # 어떤 숫자 a는 team[a]의 팀에 속한다.
# # 즉, 1은 team[1]인 1에 속하고, 2는 team[2]에 속하며, N은 team[N]에 속한다.

# # 어떤 두 숫자 a, b의 team[a], team[b]를 비교하여
# # 같다면 YES를 프린트하고 다르다면 NO를 프린트한다. (같은 팀인지 확인)
# # 같은 팀에 넣고 싶다면 두 수 중 큰 숫자의 팀을 작은 숫자의 팀에 맞춰서 바꾼다.

# parent=[i for i in range(N+1)]

# for i in range(M):
#     ornot, a, b=map(int, sys.stdin.readline().split())
#     if ornot:
#         if checkteam(parent, a)==checkteam(parent, b):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         teamup(parent, a, b)

# 2020년 11월 4일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())

parent=[i for i in range(n+1)]

def teamup(parent, a, b):
    a=checkteam(parent, a)
    b=checkteam(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def checkteam(parent, num):
    if parent[num]!=num:
        parent[num]=checkteam(parent, parent[num])
    return parent[num]

for i in range(m):
    ornot, a, b=map(int, sys.stdin.readline().split())
    if ornot:
        if checkteam(parent, a)==checkteam(parent, b):
                print("YES")
        else:
            print("NO")
    else:
        teamup(parent, a, b)