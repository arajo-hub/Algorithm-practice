def solution(priorities, location):
    answer=0
    while(len(priorities)!=0): # priorities에 출력할 문서가 있을 때,
        if location==0: # 출력순서를 알고 싶은 문서가 제일 처음에 있다고 할 때,
            if priorities[0]<max(priorities): # 그 문서보다 더 중요한 문서가 있으면
                priorities.append(priorities.pop(0)) # 그 문서는 순서를 뒤로 옮긴다.
                location=len(priorities)-1 # 그리고 location을 그 문서의 순서를 나타내도록 교체한다. (location을 볼 때는 0부터 시작되므로 -1을 해준다.)
            else: # 제일 앞에 있는 문서보다 중요한 문서가 뒤에 없다면,
                return answer+1 # 1번째라는 위치를 출력한다. 몇번째인지 위치를 말할 때는 (location처럼) 0이 아닌 1부터 시작하므로 +1을 해준다.
        else: # 출력순서를 알고 싶은 문서가 처음이 아닌 곳에 있다고 할 때,
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location-=1 # 중요도가 비교적 낮은 앞문서는 뒤로 추가되므로 location도 1칸 당겨져서 -1을 해준다.
            else:
                priorities.pop(0) # 앞문서를 출력하고,
                location-=1 # 앞문서가 출력되었으므로, location에 -1을 해준다.(즉, 한칸씩 당겨준다.)
                answer+=1 # answer는 위치를 출력하므로 +1을 해준다.
    return answer

print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([2, 1, 3, 2], 2))