def solution(number, k):
    length = len(number)
    if length > k:
        m = 0
        for cnt in range(k):
            for idx in range(m, length-1):
                if number[idx] < number[idx+1]:
                    number = number[:idx] + number[idx+1:] # number[idx]를 없앤다.
                    length -= 1
                    if idx > 0:
                        m = idx-1
                    break
            else:
                number = number[:length-k+cnt]
                break
        return "".join([str(i) for i in number])
    else:
        return "0"


print(solution([4, 1, 7, 7, 2, 5, 2, 8, 4, 1], 4))