import sys
from copy import deepcopy

n=int(sys.stdin.readline())
origin=[]

for i in range(n):
    origin.append(int(sys.stdin.readline()))

# 내 풀이

# 먼저 입력받은 수열과 같은 수열(copy)을 하나 만든다.
# 그리고 copy를 오름차순 정렬시킨다.
# copy에서 앞에서부터 숫자를 하나씩 꺼내서 stack에 append해주고 이때 cal에도 '+'를 append한다.
# 이제 만들어야 할 수열인 origin과 stack을 비교하며, origin에 들어가야할 수가 stack에 들어가있다면
# stack에서 pop을 해주고, cal에도 '-'를 append한다.
# 같은 수를 만났다면 origin의 다음 수와 stack의 마지막 수도 같은지 비교한다. (stack에서 pop했으므로 그전수가 마지막 수가 된다.)
# 같다면 pop해서 stack에 추가해주고, 인덱스를 조정하여 계속 비교한다.
# 다른 수를 만났다면 o_index는 그대로 두고 copy에서 숫자를 꺼내서 stack에 추가하는 과정으로 돌아간다.
# 이 과정이 끝났다면 1차적으로 수열을 만들 수들은 꺼냈고, stack에 남아있는 수들은 전부 pop을 통해 순서대로 꺼내야 한다.
# 그러므로 stack과 origin의 끝부분을 뒤바꾼 것(origin[:-len(stack)-1:-1])이 같다면 전부 pop을 통해 순서대로 꺼낼 수 있으므로
# cal에 ['-']*len(stack)을 extend해준다.

copy=deepcopy(origin)

copy.sort()

o_index=0
c_index=0
stack=[]
cal=[]

while(c_index!=len(copy)):
    if stack!=[] and origin[o_index]==stack[-1]:
        stack.pop(-1)
        cal.append('-')
        o_index+=1
    else:
        stack.append(copy[c_index])
        cal.append('+')
        c_index+=1

if (stack==origin[:-len(stack)-1:-1]):
    cal.extend(['-']*len(stack))
    for c in cal:
        print(c)
else:
    print("NO")

# 다른 풀이

# import sys

# input = sys.stdin.readline

# n = int(input())
# origin = [int(input()) for _ in range(n)] # 주어진 수열

# def sol():

#     result=[]
#     stack=[]
#     pointer = 1

#     for i in range(n): # 수열의 길이만큼 돌면서

#         num = origin[i] # 숫자 하나를 꺼내서.
#         for j in range(pointer, num+1): # stack에 push한다.
#             stack.append(j)
#             result.append('+')
#             pointer += 1

#         result.append('-') # result에 '-'를 추가해주고

#         if origin[i] != stack.pop(): # stack에서 뽑아낸 마지막 수와 꺼낸 수가 같지 않다면 'NO'
#             return 'NO'

#     return '\n'.join(result)

# print(sol())