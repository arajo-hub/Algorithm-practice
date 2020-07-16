def solution(scoville, K):
    import heapq
    cnt=0
    heapq.heapify(scoville) # scoville을 heap으로 만들어주고
    while True:
        first=heapq.heappop(scoville) # heap에서 먼저 꺼낸 값을 first에 저장
        if first>=K: # first가 K보다 크다면(=scoville에서 가장 작은 값이 K보다 크다면)
            break # 멈춘다
        if len(scoville)==0: # scoville에 더이상 아무것도 남아있지 않다면
            return -1 # -1을 return
        second=heapq.heappop(scoville) # 위 조건에 걸리지 않고(=계속 진행 가능할 때) second에 두번째로 꺼낸 값(=scoville에서 두번째로 작은 값)을 저장
        heapq.heappush(scoville, first+second*2) # scoville에 first+second*2의 값을 넣어준다.
        cnt+=1 # 위의 한 번의 과정을 거쳤으므로 +1
    return cnt