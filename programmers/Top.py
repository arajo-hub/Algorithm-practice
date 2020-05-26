def solution(heights):
    answer = [0] * len(heights) # heights의 길이만큼의 list인 answer를 생성해준다.
    while heights:
        index=heights.pop() # 오른쪽에서부터 값을 하나 뽑아서 그 값을 제외한 리스트 중 index보다 값이 큰 수를 찾는다.
        print(index, heights)
        for i in range(len(heights)-1, -1, -1): # i는 리스트의 인덱스값으로 사용되므로 -1을 해주고, 마지막값은 인덱스의 마지막값인 0이 되어야하므로 -1로 해준다.
            if heights[i]>index: # index 왼쪽의 리스트의 값들 중 index보다 큰 값을 찾으면,
                answer[len(heights)]=i+1 # answer리스트에 i+1를 넣어준다.
                print(answer)
                break
    return answer