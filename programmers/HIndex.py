def solution(citations):
    for index, count in enumerate(sorted(citations)):
        if count>=len(citations)-index:
            return len(citations)-index
    return 0

# 파이썬 내장함수 중 enumerate는 순서가 있는 자료형을 입력으로 받아 index값과 각 개체값을 포함하는 enumerate객체로 돌려준다.
# 예를 들면,
# for index, name in enumerate(['김철수', '박영희', '홍길동']):
#     print(index, name)
# 결과값은
# 0 김철수
# 1 박영희
# 2 홍길동

# 위 설명의 출처는 https://wikidocs.net/32#enumerate