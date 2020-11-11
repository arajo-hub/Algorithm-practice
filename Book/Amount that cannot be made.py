# import sys

# N=int(sys.stdin.readline())

# nums=list(map(int, sys.stdin.readline().split()))
# nums.sort()

# goal=1

# for i in nums:
#     if goal<i:
#         break
#     goal+=i

# print(goal)

# # 만약 5개의 숫자 6, 1, 4, 5, 2가 있다면 이를 정렬한다.
# # 1, 2, 4, 5, 6
# # 만들 수 없는 최소값을 찾기 위해서는 1부터 시작해야 하므로
# # goal을 1로 설정하고,
# # goal이 i보다 작은 값이라면 끝나도록 설계한다.
# # goal이 i와 같거나 i보다 큰 값이라면 goal에 i를 더한다.

# # goal=1, i=1 : goal이 i와 같으므로 pass. 1를 더해서 goal은 2가 된다.
# # goal=2, i=2 : goal이 i와 같으므로 pass. 2를 더해서 goal은 4가 된다.
# # 여기서 잠깐, 만약 i가 3이었다면(goal=2, i=3), goal이 i보다 작기 때문에 break가 된다. 만들 수 없는 최소값은 goal인 2가 된다.
# # 다시 돌아와서, goal=4, i=4 : goal이 i와 같으므로 pass. 4를 더해서 goal은 8이 된다.
# # goal=8, i=5 : goal이 i보다 크므로 pass. 5를 더해서 goal은 13이 된다.
# # goal=13, i=6 : goal이 i보다 크므로 pass. 6을 더해서 goal은 19가 된다.

# 2020년 11월 11일 풀이

import sys

n=int(sys.stdin.readline())

coins=list(map(int, sys.stdin.readline().split()))

coins.sort()

goal=1

for coin in coins:
    if goal<coin:
        break
    goal+=coin

print(goal)