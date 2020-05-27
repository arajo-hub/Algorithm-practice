def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge=[0]*bridge_length # 다리의 길이가 2이면 [0, 0], 3이면 [0, 0, 0]과 같은 다리의 형태를 만들어준다.
    while bridge:
        answer+=1 # 시간이 1씩 흐를 때마다 다리의 상태를 변화시켜준다.
        bridge.pop(0) # 다리 끝에 있는 트럭을 다리밖으로 옮겨주는 역할이다.
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight: # 다리에 올라와있는 트럭의 무게와 새로 올라갈 트럭의 무게를 합쳐서 기준무게보다 작다면,
                bridge.append(truck_weights.pop(0)) # 다리의 끝부분에 새로운 트럭을 올려준다.
            else: # 만약 기준무게를 넘는다면,
                bridge.append(0) # 다리의 끝에 [0]을 추가해서 완벽히 빈 다리를 만들어준다.
    return answer

print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(solution(3, 5, [4]))