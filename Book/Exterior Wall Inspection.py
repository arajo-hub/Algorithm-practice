from itertools import permutations

def solution(n, weak, dist): # n은 외벽의 길이, weak는 취약 지점의 위치가 담긴 배열, dist는 각 친구가 1시간동안 이동할 수 있는 거리
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n) # 원형으로 구성되어있다고 하므로 편의상 길이를 2배로 늘려서 원형을 일자로 만들어준다.
    answer=len(dist)+1 # 투입할 친구의 최솟값을 찾을 때, count와 비교해야 하므로 총 친구들 수보다 +1을 해준다.
    for start in range(length): # 취약 지점을 하나씩 뽑아
        for friends in list(permutations(dist, len(dist))): # permutations는 친구들을 줄세우는 모든 경우의 수를 반환한다.(순열)
            count=1 # 투입할 친구의 수
            position=weak[start]+friends[count-1] # 해당 친구가 점검할 수 있는 마지막 위치
            for index in range(start, start+length): # 시작지점부터 모든 취약 지점을 확인한다.
                if position < weak[index]: #해당 친구가 점검할 수 있는 마지막 위치를 벗어난 경우
                    count+=1 # 새로운 친구를 넣고
                    if count>len(dist): # 더 투입이 불가능하다면 종료한다.
                        break
                    position=weak[index]+friends[count-1] # 새로운 친구를 넣었을 때, 그 친구가 점검할 수 있는 마지막 위치
            answer=min(answer, count) # 최솟값을 찾는다.
    if answer>len(dist):
        return -1
    return answer

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))