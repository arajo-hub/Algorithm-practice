# 아이디 길이를 3자 이상 15자 이하
# 알파벳 소문자, 숫자, -, _, . 만 사용 가능
# . 는 처음과 끝에 사용할 수 없고, 연속으로 사용할 수 없음

def solution(new_id):

    # 1단계
    # 모든 대문자를 소문자로
    new_id = new_id.lower()

    # 2단계
    # 알파벳 소문자, 숫자, -, _, . 만 사용 가능
    answer = ''
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word

    # 3단계
    # 마침표 2번 이상 연속 -> 하나의 마침표로
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계
    # 마침표가 처음이나 끝에 있다면 제거
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    # 5단계
    # 빈 문자열이라면 'a' 대입
    answer = 'a' if answer == '' else answer

    # 6단계
    # 길이가 16자 이상이라면 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    # 제거 후 마침표가 new_id의 끝에 위치한다면 마침표도 제거
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    # 길이가 2자 이하라면 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임.
    if len(answer) < 3:
        answer = answer + answer[-1] * (3-len(answer))
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))