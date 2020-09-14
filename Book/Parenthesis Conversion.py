def balanced_index(p): # 괄호의 개수가 같은지 확인.
    count=0
    for i in range(len(p)):
        if p[i]=='(': # '('이 나오면 +1
            count+=1
        else:
            count-=1 # ')'이 나오면 -1
        if count==0: # '('과 ')'의 개수가 같으면
            return i # 같아지는 부분의 바로 다음 인덱스를 리턴.

def check_proper(p): # 괄호가 제대로 짝을 짓고 있는지 확인
    count=0
    for i in p: # 문자열에서 하나씩 꺼내서
        if i=='(': # '('과 같다면 +1
            count+=1
        else: # ')'일 때
            if count==0: # count가 0이면(즉, 이 앞까지는 잘 맞았음) 제대로 짝을 짓고 있지 않다는 것이므로
                return False # False 리턴.
            count-=1 # ')'이고 count가 0이 아니면 -1
    return True # 문자열 끝까지 진행되고 직전에 count가 0이 아니었다면 True 리턴.

def solution(p):
    answer=''
    if p=='': # 입력한 문자열이 빈 문자열이라면
        return answer # 빈 문자열 그대로 반환
    index=balanced_index(p) # '('과 ')'의 개수가 같아지는 위치의 바로 다음 인덱스를 index에 저장
    left=p[:index+1] # u에는 index까지,
    right=p[index+1:] # v에는 index이후까지를 나눠서 담는다.
    if check_proper(left): # index기준 왼쪽문자열 괄호가 제대로 짝을 짓고 있는지 확인.
        answer=left+solution(right) # 재귀함수로 u문자열을 자르면서 확인
    else: # index기준 왼쪽문자열 괄호가 제대로 짝을 짓고 있지 않다면,
        answer='(' # 제일 먼저 '('를 넣어주고
        answer+=solution(right) # 재귀함수로 v문자열을 자르면서 확인
        answer+=')' # 마지막으로 ')'를 넣어준다.
        left=list(left[1:-1]) # index기준 왼쪽문자열의 첫번째와 마지막 문자를 제거.
        for i in range(len(left)):
            if left[i]=='(': #'('를
                left[i]=')' # ')'로 바꿔주고
            else: # ')'이라면
                left[i]='(' # '('로 바꿔준다.
        answer+="".join(left)
    return answer