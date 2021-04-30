# from collections import deque

# def solution(numbers, target):
    
#     answer = 0

#     # 큐를 만든다.
#     q = deque()

#     length = len(numbers)

#     # +인 값과 -인 값을 넣어준다.
#     q.append([numbers[0], 0])
#     q.append([-1*numbers[0], 0])

#     while q:

#         # 큐에서 값을 꺼내서 이 값으로 다음 단계의 값을 만든다.
#         value, index = q.popleft()

#         # 다음 단계로 이동한 셈.
#         index += 1

#         if index < length:
#             # 다음 단계의 +, -값을 만들어서 큐에 넣는다.
#             q.append([value + numbers[index], index])
#             q.append([value - numbers[index], index])
#         else:
#             if value == target:
#                 answer += 1
            
#     return answer

# 좀 더 간결한 풀이(출처 : 프로그래머스)

def solution(numbers, target):
    # numbers가 비어있고 target이 0이면 1
    if not numbers and target == 0 :
        return 1
    # number가 비어있고 target이 0이 아니면 0
    elif not numbers:
        return 0
    # numbers가 비어있지 않으면 아래 코드 실행
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 예를 들어,
# [1, 1, 1, 1, 1]로 3을 만드는 방법은
# [1, 1, 1, 1]로 2를 만드는 방법에 1을 더한 것과
# [1, 1, 1, 1]로 4를 만든느 방법에 1을 뺀 것과 같다.

# [1, 1, 1, 1, 1]로 3을 만드는 방법
# = ( [1, 1, 1, 1]로 2를 만드는 방법에 1(list[0])을 더한 것 ) + ( [1, 1, 1, 1]로 4를 만드는 방법에 1(list[0])을 뺀 것)
# 4 + 1 = 5

# [1, 1, 1, 1]로 2를 만드는 방법 -> 4
# = ( [1, 1, 1]로 1을 만드는 방법에 1(list[1])을 더한 것 ) + ( [1, 1, 1]로 3을 만드는 방법에 1(list[1]을 뺀 것)
# 3 + 1 = 4

# [1, 1, 1, 1]로 4를 만드는 방법 -> 1
# = ( [1, 1, 1]로 3을 만드는 방법에 1(list[1])을 더한 것 ) + ( [1, 1, 1]로 5를 만드는 방법에 1(list[1])을 뺀 것)
# 1 + 0 -> 1

# [1, 1, 1]로 1을 만드는 방법 -> 3
# = ( [1, 1]로 0을 만드는 방법에 1을 더한 것 ) + ( [1, 1]로 2를 만드는 방법에 1을 뺀 것 )
# 2 + 1 = 3

# [1, 1, 1]로 3을 만드는 방법 -> 1
# = ( [1, 1]로 2를 만드는 방법에 1을 더한 것 ) + ( [1, 1]로 4를 만드는 방법에 1을 뺀 것 )
# 1 + 0 = 1

# [1, 1, 1]로 5를 만드는 방법 -> 0
# = ( [1, 1]로 4를 만드는 방법에 1을 더한 것 ) + ( [1, 1]로 6을 만드는 방법에 1을 뺀 것 )
# 0 + 0 = 0

# [1, 1]로 0을 만드는 방법 -> 2
# = ( [1]로 -1를 만드는 방법에 1을 더한 것 ) + ( [1]로 1을 만드는 방법에 1을 뺀 것 )
# 1 + 1 = 2

# [1, 1]로 2를 만드는 방법 -> 1
# = ( [1]로 1을 만드는 방법에 1을 더한 것 ) + ( [1]로 3을 만드는 방법에 1을 뺀 것 )
# 1 + 0 = 1

# [1, 1]로 4를 만드는 방법 -> 0
# = ( [1]로 3을 만드는 방법에 1을 더한 것 ) + ( [1]로 5를 만드는 방법에 1을 뺀 것 )
# 0 + 0 = 0

# [1, 1]로 6을 만드는 방법 -> 0
# = ( [1]로 5를 만드는 방법에 1을 더한 것 ) + ( [1]로 7을 만드는 방법에 1을 뺀 것 )
# 0 + 0 = 0

# [1]로 -1를 만드는 방법 -> 1
# = ( []로 -2를 만드는 방법에 1을 더한 것 ) + ( []로 0을 만드는 방법에 1을 뺀 것 )
# = solution([], -2]) -> 0 반환
# = solution([], 0]) -> 1 반환

# [1]로 1을 만드는 방법 -> 1
# = ( []로 0을 만드는 방법에 1을 더한 것 ) + ( []로 2를 만드는 방법에 1을 뺀 것 )
# = solution([], 0]) -> 1 반환
# (*** 리스트가 비어 있고 target이 0이면 1, 리스트가 비어 있고 target이 0이 아니면 0)
# = solution([], 2]) -> 0 반환

# [1]로 3을 만드는 방법 -> 0
# = ( []로 2를 만드는 방법에 1을 더한 것 ) + ( []로 4를 만드는 방법에 1을 뺀 것 )
# = solution([], 2]) -> 0 반환
# = solution([], 4]) -> 0 반환

# [1]로 5를 만드는 방법 -> 0
# = ( []로 4를 만드는 방법에 1을 더한 것 ) + ( []로 6을 만드는 방법에 1을 뺀 것 )
# = solution([], 4]) -> 0 반환
# = solution([], 6]) -> 0 반환

# [1]로 7을 만드는 방법 -> 0
# = ( []로 6을 만드는 방법에 1을 더한 것 ) + ( []로 8을 만드는 방법에 1을 뺀 것 )
# = solution([], 6]) -> 0 반환
# = solution([], 8]) -> 0 반환

print(solution([1, 1, 1, 1, 1], 3))