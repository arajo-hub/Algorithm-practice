def solution(n):
    result=[]
    if n==1:
        result.append(0)
    else:
        result.extend(solution(n-1))
        result.append(0)
        for j in range(len(result)-2, -1, -1):
            if result[j]==1:
                result.append(0)
            else:
                result.append(1)
    return result

# 1번 접었을 때에는 [0]
# 2번 접었을 때에는 [0, 0, 1]
# 3번 접었을 때에는 [0, 0, 1, 0, 0, 1, 1]
# 4번 접었을 때에는 [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
# 이 된다.
# 규칙을 찾아보면, 그 전단계에서 0을 추가하고, 그 이후는 그 전단계의 좌우대칭의 반대값임을 알 수 있다.
# 종이접기를 해보면 0인 부분과 겹쳐지던 부분은 1이 되는 원리.
# 그렇기 때문에 나는 재귀함수를 이용하여 결과에 0을 추가하고 그 이후로는 for문으로 반대값을 추가하는 식으로 문제를 풀었다.
# 하지만 아래와 같이 간단한 코드풀이도 있다.
#
# def solution(n):
#     fold = 0
#     arr = [fold]
#
#     for i in range(n - 1): # n-1번만큼 아래의 식을 반복한다.
#         arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]] # arr은 항상 왼쪽에 고정이고, 0을 추가한 다음(+ [fold]), arr을 거꾸로 돌려 비트로 반대값을 출력한다.
#
#     return arr