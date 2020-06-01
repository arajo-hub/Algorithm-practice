def solution(n, times):
    best=(min(times)*n)/len(times) # 입국심사가 완료되는 최단시간은 제일 빠른 심사원이 모든 사람을 처리했을 때이고,
    worst=(max(times)*n)/len(times) # 입국심사가 완료되는 최장시간은 제일 느린 심사원이 모든 사람을 처리했을 때이다.
    # 우리가 원하는 답은 best와 worst 사이에 있다.

    def find(b, w):
        if b==w: # 만약 best와 worst가 같다면, 답은 그 값이 된다.
            return b
        mid=int((b+w)/2) # 하지만 그렇지 않으면, best와 worst의 중간값을 찾아준다.
        nSum=0
        for time in times: # 그리고 times리스트를 돌리면서
            nSum+=mid//time # best와 worst의 중간값을 각 시간으로 나눈 몫을 nSum에 더해준다.
            if nSum>n: # 만약 nSum이 n보다 크다면(=즉, 시간내에 처리할 수 있는 인원수가 현재 대기중인 인원수보다 많다면 멈춘다.)
                break
        if nSum>=n: # 만약 nSum이 n보다 크거나 같다면(=즉, 시간내에 처리할 수 있는 인원수가 현재 대기중인 인원수보다 많다면), 재귀함수를 이용해 최소시간과 중간값사이에서 최적의 시간을 찾는다.
            return find(b, mid)
        else: # nSum이 n보다 작다면(=즉, 시간내에 처리할 수 있는 인원수가 현재 대기중인 인원수보다 적다면), 재귀함수를 이용해 중간값과 최장시간사이에서 최적의 시간을 찾는다.
            return find(mid+1, w)

    answer=find(best, worst)
    return answer