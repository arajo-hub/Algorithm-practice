# # 이 문제의 경우, 이전에 풀었던 문제인 상하좌우(Up Down Left Right)와 풀이법이 유사하다.
# # 설명이 복잡하게 되어있지만, 한 점을 기준으로 가능한 경우의 수를 정리하면 아래와 같다.

# # 1번째, x는 +1 y는 -2
# # 2번째, x는 +2 y는 -1
# # 3번째, x는 +2 y는 +1
# # 4번째, x는 +1 y는 +2
# # 5번째, x는 -1 y는 +2
# # 6번째, x는 -2 y는 +1
# # 7번째, x는 -2 y는 -1
# # 8번째, x는 -1 y는 -2

# # 결과적으로 최대 8가지 경우가 나온다는 것을 알 수 있다.

# # 결국 이 문제의 해법은
# # 기준이 되는 x, y에 첫번째 경우를 대입하고 8*8의 좌표평면 안에 있는지 테스트하고,
# # 좌표평면 밖에 있다면 count에서 제외하고, 이렇게 여덟번째 경우까지 반복하는 것이다.

# import sys

# knight=sys.stdin.readline()
# rows=[0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # 문제에서 규정해주었고, 변화가 있다는 이야기는 없으므로 그냥 a, b, c, ... 그대로 사용한다.
# x=rows.index(knight[0]) # 위의 rows 리스트에서 knight의 가로위치(알파벳)을 찾아 숫자로 변환. 후에 숫자 연산을 해줘야 하기 때문.
# y=int(knight[1]) # 입력받은 knight의 세로위치.

# dx=[1, 2, 2, 1, -1, -2, -2, -1]
# dy=[-2, -1, 1, 2, 2, 1, -1, -2]

# cnt=0

# for i in range(8):
#     new_x=x+dx[i]
#     new_y=y+dy[i]
#     if new_x<=0 or new_y<=0 or new_x>8 or new_y>8:
#         continue
#     cnt+=1

# print(cnt)

# 2020년 10월 19일 풀이

import sys

alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g']
where=sys.stdin.readline()
a=alpha.index(where[0])
b=int(where[1])

dx=[1, -1, 1, -1, 2, 2, -2, -2]
dy=[2, -2, -2, 2, 1, -1, 1, 1]

x, y=a+1, b

cnt=0
for i in range(8):
    new_x, new_y=x+dx[i], y+dy[i]
    if new_x<1 or new_x>8 or new_y<1 or new_y>8:
        continue
    cnt+=1

print(cnt)