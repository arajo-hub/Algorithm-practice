def solution(N, stages):
    failure=[]
    length=len(stages)

    for i in range(1, N+1):
        count=stages.count(i)
        if length==0:
            fail=0
        else:
            fail=count/length

        failure.append((fail, i))
        length-=count

    failure.sort(key=lambda x:(-x[0], x[1]))

    result=[j[1] for j in failure]
    return result