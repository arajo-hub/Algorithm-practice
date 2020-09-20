def solution(N, stages):
    failure=[]
    cnt=len(stages)

    for i in range(1, N+1):
        count=stages.count(i)
        if cnt==0:
            fail=0
        else:
            fail=count/cnt

        failure.append((fail, i))
        cnt-=count

    failure.sort(key=lambda x:(-x[0], x[1]))

    result=[j[1] for j in failure]
    return result