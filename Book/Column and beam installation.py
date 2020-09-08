def possible(answer):
    for x, y, stuff in answer: # answer에 있는 x좌표, y좌표, 기둥인지 보인지(stuff)를 꺼내어 확인
        if stuff ==0: # stuff가 기둥일 때
            if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                # 바닥이거나(y==0),
                # 보의 한쪽 끝부분 위거나([x-1, y, 1] in answer or [x, y, 1] in answer),
                # 다른 기둥 위([x, y-1, 0)라면
                continue # 계속 반복
            return False # 위의 경우가 아니라면 return False
        elif stuff==1: # stuff가 보라면
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                # 한쪽 끝부분이 기둥 위거나([x, y-1, 0] in answer or [x+1, y-1, 0] in answer),
                # 양쪽 끝부분이 다른 보와 동시에 연결되어있다면([x-1, y, 1] in answer and [x+1, y, 1] in answer),
                continue # 계속 반복
            return False # 위의 경우가 아니라면 return False
    return True # 반복문이 끝날 때까지 위의 경우들에 속하지 않으면 return True

def solution(n, build_frame):
    answer=[]
    for frame in build_frame:
        x, y, stuff, operate=frame # 실행순서에서 x좌표, y좌표, 기둥인지 보인지(stuff), 설치인지 삭제인지(operate)를 꺼낸다.
        if operate==0: # 설치하는 경우라면
            answer.remove([x, y, stuff]) # 일단 삭제하고
            if not possible(answer): # 가능한 경우인지 확인
                answer.append([x, y, stuff]) # 가능한 경우가 아니라면 다시 설치
        if operate==1: # 삭제하는 경우라면
            answer.append([x, y, stuff]) # 일단 설치하고
            if not possible(answer): # 가능한 경우인지 확인
                answer.remove([x, y, stuff]) #가능한 경우가 아니라면 다시 삭제
    return sorted(answer) # 정렬된 결과 반환