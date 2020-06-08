def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion) :
        if i != j :
            return i
    return participant[-1]

# 아래는 파이썬의 collections라는 모듈을 이용하여 푸는 방법이다.
# collenctions에 대해 알아둘 것.

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]