import heapq

def solution(food_times, K):
    if sum(food_times)<=K:
        return -1
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    sum_value=0
    previous=0
    length=len(food_times)
    while sum_value+((q[0][0]-previous)*length)<=K:
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        length-=1
        previous=now
    result=sorted(q, key=lambda x:x[1])
    return result[(K-sum_value)%length][1]