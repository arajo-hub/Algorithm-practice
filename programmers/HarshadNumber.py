def solution(x):
    arr = list(str(x))
    result = 0
    
    for i in range(len(arr)):
        result += int(arr[i])
        if x % result == 0:
            answer = True
        else: answer = False
    
    return answer