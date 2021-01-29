# n, m = map(int, input().split())
# idx = list(map(int, input().split()))

# step = 0


# def move_left(que):
#     global step
#     step += 1

#     tmp = que.pop(0)
#     que.append(tmp) # 제일 앞에 있는 수를 제일 뒤로 가져온다.


# def move_right(que) # 그 수가 제일 앞에 올 때까지 오른쪽으로 이동:
#     global step
#     step += 1

#     tmp = [que.pop(-1)]
#     tmp.extend(que) # 제일 뒤에 있는 값을 앞으로 가져온다.
#     que = tmp

#     return que


# # que 만들기
# que = list(range(1, n + 1))

# # 원하는 수를 다 뽑을 때까지 반복
# while idx:
#     if que[0] == idx[0]:
#         que.pop(0)
#         idx.pop(0)
#     else:
#         # 움직인다.
#         if que.index(idx[0]) <= len(que) // 2: # 찾아야할 수가 중간을 기준으로 왼쪽에 있다면
#             while que[0] != idx[0]: move_left(que) # 그 수가 제일 앞에 올 때까지 왼쪽으로 이동
#         else: # 찾아야할 수가 중간을 기준으로 오른쪽에 있다면
#             while que[0] != idx[0]: que = move_right(que) # 그 수가 제일 앞에 올 때까지 오른쪽으로 이동

# print(step)

# 2021년 1월 29일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())
# n은 큐의 크기, m은 뽑아내려고 하는 수의 개수

array=list(map(int, sys.stdin.readline().split()))

# 큐 만들기
que=[i for i in range(1, n+1)]

def left(): # 왼쪽으로 한 칸 이동
    global que
    num=que.pop(0)
    que.append(num)

def right(): # 오른쪽으로 한 칸 이동
    global que
    num=[que.pop(-1)]
    num.extend(que)
    que=num
    

count=0
a_index=0
while (True):
    if a_index==len(array):
        break
    if que[0]==array[a_index]:
        que.pop(0)
        a_index+=1
    elif (que.index(array[a_index]))<(len(que)-que.index(array[a_index])):
        left()
        count+=1
    elif (que.index(array[a_index]))>=(len(que)-que.index(array[a_index])):
        right()
        count+=1

print(count)

# 1월 29일의 풀이
# count=0
# a_index=0
# while (True):
#     if a_index==len(array): # 여기에서는 array는 그대로 두고 index만 이용했는데, 아래처럼 숫자뽑을 때 array에서도 숫자를 같이 뽑는 식으로 했으면 좋았을 것 같다.
#         break
#     if que[0]==array[a_index]:
#         que.pop(0)
#         a_index+=1
#     elif (que.index(array[a_index]))<(len(que)-que.index(array[a_index])):
#     # 이 부분도 찾아야할 수의 위치를 기준으로 왼쪽인지 오른쪽인지 간단하게 찾았으면 좋았을 것 같다.
#         left()
#         count+=1
#     elif (que.index(array[a_index]))>=(len(que)-que.index(array[a_index])):
#         right()
#         count+=1

# 이전의 풀이

# while idx:
#     if que[0] == idx[0]:
#         que.pop(0)
#         idx.pop(0)
#     else:
#         # 움직인다.
#         if que.index(idx[0]) <= len(que) // 2: # 찾아야할 수가 중간을 기준으로 왼쪽에 있다면
#             while que[0] != idx[0]: move_left(que) # 그 수가 제일 앞에 올 때까지 왼쪽으로 이동
#         else: # 찾아야할 수가 중간을 기준으로 오른쪽에 있다면
#             while que[0] != idx[0]: que = move_right(que) # 그 수가 제일 앞에 올 때까지 오른쪽으로 이동