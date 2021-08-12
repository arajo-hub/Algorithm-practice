def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer

# 출처 : https://ykss.netlify.app/algorithm/programmers_66/