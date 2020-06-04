def solution(numbers):
    numbers=[str(x) for x in numbers]
    numbers.sort(key=lambda x:(x*4)[:4], reverse=True)
    answer="".join(numbers) if numbers[0]!="0" else "0"
    return answer

# 출처 : https://gurumee92.tistory.com/161
# 위 방법은 numbers가 [3, 30, 34, 5, 9]로 주어졌을 때,
# 각 요소를 3333, 3030, 3434, 5555, 9999 식으로 만들어서(문제조건에서 numbers의 요소는 0~1,000까지라는 조건이 있음)
# 그 값의 순서에 따라 배열하는 방법이다.
# 실제로 배열해보면, 9999, 5555, 3434, 3333, 3030이 되고, 이를 원래의 숫자로 바꿔보면 9, 5, 34, 3, 30이 된다.