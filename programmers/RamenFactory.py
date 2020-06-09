import heapq

def solution(stock, dates, supplies, k):
    answer, start = 0, 0
    x=[]
    while stock < k:
        for i in range(start, len(dates)):
            if dates[i]<=stock:
                heapq.heappush(x, (-supplies[i], supplies[i]))
                start=i+1
            else:
                break
        answer+=1
        stock+=heapq.heappop(x)[1]
    return answer