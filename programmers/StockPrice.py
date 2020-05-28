def solution(prices):
    answer = [0]*len(prices) # 입력한 주식가격의 갯수만큼의 공간을 가진 리스트를 만든다.
    for i in range(len(prices)-1): #prices에 있는 주식가격의 갯수만큼 for문을 돌리는데,
        for j in range(i, len(prices)-1): # 하나의 가격마다 그 다음 가격들과 비교한다.
            if prices[i]>prices[j]:
                break
            else:
                answer[i] +=1
    return answer