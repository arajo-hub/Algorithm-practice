def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion) :
        if i != j :
            return i
    return participant[-1]