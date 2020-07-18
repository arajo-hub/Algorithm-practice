def solution(answers):
    score={1:0, 2:0, 3:0} # 1번 수포자, 2번 수포자, 3번 수포자까지로 참가하는 인원이 정해져있고, 이 이상 추가될 예정이 없으므로 dict을 다음과 같이 선언해준다.
    answer=[] # 나중에 가장 많이 맞은 수포자만 모아서 출력하기 위해 answer 리스트를 만들어준다.

    one=([1, 2, 3, 4, 5]*len(answers))[:len(answers)] # 1번 수포자는 1, 2, 3, 4, 5가 반복되는 방식을 쓰므로 answers길이만큼 반복해서 만들어주되, len(answers)길이만큼 자른다.
    two=([2, 1, 2, 3, 2, 4, 2, 5]*len(answers))[:len(answers)] # 위와 마찬가지로 같은 방법으로 2번 수포자의 답안지를 만든다.
    three=([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*len(answers))[:len(answers)] # 3번 수포자도 마찬가지.

    for i in range(len(answers)): # answers의 답과 1번, 2번, 3번 수포자 각각의 답안지와 비교한다.
        if answers[i]==one[i]: # 답안이 같은 사람이 있다면 그 수포자의 점수를 1점 올려준다.
            score[1]+=1
        if answers[i]==two[i]:
            score[2]+=1
        if answers[i]==three[i]:
            score[3]+=1

    for key, value in score.items():
        if value==max(score.values()): # score에 있는 value(점수) 중 가장 큰 값과 value가 같으면
            answer.append(key) # answer에 key(몇번째 수포자인지)를 추가한다.
    return answer