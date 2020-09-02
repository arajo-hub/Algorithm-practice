import heapq

def solution(food_times, K):
    if sum(food_times)<=K: # 음식들을 전부 먹는 데 걸리는 시간보다 방송이 중단된 시간(K)가 길다면 -1을 반환.
        return -1
    q=[] # 빨리 먹을 수 있는 음식 순서대로 남을 q를 만든다.
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1)) # (음식을 먹는 데 걸리는 시간, 몇 번째 음식인지)를 저장.
    sum_value=0
    previous=0
    length=len(food_times)
    while sum_value+((q[0][0]-previous)*length)<=K:
        now=heapq.heappop(q)[0] # 빨리 먹을 수 있는 순서대로 음식을 먹는 데 걸리는 시간(now)을 꺼낸다.
        sum_value+=(now-previous)*length # now에서 이전까지 걸린 시간을 빼서 음식의 개수를 곱한다.
        length-=1 # 한 음식을 다 먹은 게 되므로 -1을 해준다.
        previous=now # now를 previous에 저장해준다.
    result=sorted(q, key=lambda x:x[1]) # 음식 원래 순서대로 정렬
    return result[(K-sum_value)%length][1]