# def solution(N, stages):
#     failure=[]
#     length=len(stages) # 실패율 계산에서 분모가 될 부분

#     for i in range(1, N+1):
#         count=stages.count(i) # 실패율 계산에서 분자가 될 부분
#         if length==0:
#             fail=0
#         else:
#             fail=count/length

#         failure.append((fail, i))
#         length-=count

#     failure.sort(key=lambda x:(-x[0], x[1]))

#     result=[j[1] for j in failure]
#     return result

# 2020년 12월 1일 풀이

# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수, 스테이지에 도달한 플레이어의 수
def solution(n, stages): # 스테이지의 개수 n, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
    failure=[] # 결과값을 담을 배열
    # 1단계는 1개, 1/8
    # 2단계는 3개, 3/7
    # 3단계는 2개, 2/4
    # 4단계는 1개, 1/2
    # 5단계는 0개, 100
    total=len(stages) # 실패율에서 전체 경우의 수를 나타냄. 분모.
    for i in range(1, n+1): # n단계까지 for문을 돌린다.
        ########### 0에 대한 예외처리 따로 해줄 것!
        if stages.count(i)==0:
            failureRate=0
        else:
            failureRate=stages.count(i)/total
        ###########
        failure.append((failureRate, i)) # 각 단계별로 실패율을 계산해서 몇 단계인지도 함께 배열에 넣는다.
        total-=stages.count(i) # 이미 지난 단계는 total에서 개수를 빼준다.
    failure.sort(key=lambda x:(-x[0], x[1]))
    result=[x[1] for x in failure]
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))