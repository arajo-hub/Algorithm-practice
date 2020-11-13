# import heapq

# def solution(food_times, K):
#     if sum(food_times)<=K: # 음식들을 전부 먹는 데 걸리는 시간보다 방송이 중단된 시간(K)가 길다면 -1을 반환.
#         return -1
#     q=[] # 빨리 먹을 수 있는 음식 순서대로 남을 q를 만든다.
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i+1)) # (음식을 먹는 데 걸리는 시간, 몇 번째 음식인지)를 저장.
#     sum_value=0
#     previous=0
#     length=len(food_times)
#     while sum_value+((q[0][0]-previous)*length)<=K:
#         now=heapq.heappop(q)[0] # 빨리 먹을 수 있는 순서대로 음식을 먹는 데 걸리는 시간(now)을 꺼낸다.
#         sum_value+=(now-previous)*length # now에서 이전까지 걸린 시간을 빼서 음식의 개수를 곱한다.
#         length-=1 # 한 음식을 다 먹은 게 되므로 -1을 해준다.
#         previous=now # now를 previous에 저장해준다.
#     result=sorted(q, key=lambda x:x[1]) # 음식 원래 순서대로 정렬
#     return result[(K-sum_value)%length][1]

# 2020년 11월 13일 풀이

import heapq

# food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식 번호 순서대로 들어있는 배열
# k는 방송이 중단된 시각. k초에 방송이 중단.
def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    q=[] # 빨리 먹을 수 있는 음식 순서대로 담을 q
    # 시간이 적게 걸리는 음식부터 먹도록 해야하므로 q에 정리해서 넣어준다.
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # 음식을 먹는 데 걸리는 시간과 그 음식의 번호를 저장
        sumValue=0 # 먹기 위해 사용한 시간
        previous=0 # 직전 음식을 다 먹는 데 걸린 시간
        length=len(food_times) # 남은 음식의 개수
        # 먹기 위해 사용한 시간에 현재 음식을 먹는 데에만 걸리는 시간을 더하고 현재 음식 개수를 곱하면
        # 현재 음식까지 다 먹는 데 걸리는 시간이 나온다. 이 값이 k보다 크면
        # 이 음식이 남은 음식 중 몇 번째 음식인지 확인해서 출력한다.
    while sumValue+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0] # 순서대로 음식을 꺼내오는데, 꺼내는 값은 정확하게 말하자면 그 음식을 먹는 데 걸리는 시간.
        sumValue+=(now-previous)*length # 현재 음식을 다 먹는 데에 걸리는 시간을 sumValue(먹기 위해 사용한 시간)에 더해준다.
        length-=1 # 한 음식을 다 먹었으므로 음식 1개를 빼준다.
        previous=now # 현재 음식을 다 먹었으므로 previous에 현재 음식만 다 먹는 데 걸린 시간을 저장해준다.
    result=sorted(q, key=lambda x:x[1]) # q를 음식의 번호 기준으로 정렬하고
    return result[(k-sumValue)%length][1] # 남은 음식 중 몇 번째 음식인지 확인하여 출력
    # (k-sumValue)%length : 종료시간에서 음식을 먹은 시간을 빼면 남은 시간이 나온다.
    # 1초마다 먹고 음식을 넘기므로 그 시간을 남은 음식의 개수(length)로 나누면 어떤 음식을 먹어야할지 나온다.
