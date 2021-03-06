def Hanoi(n, a, b, c): # 원판을 옮기는 순서를 출력하는 함수
    if n>20: # 원판 개수가 20개가 넘어가면 아무것도 출력하지 않는다.
        return
    if(n == 1): # 원판이 1개일 경우,
        print(a, c, sep = " ") # 원판을 그냥 세번째 탑으로 옮기면 되므로 1 3 의 형태로 출력한다. 첫번째 탑의 원판을 세번째 탑으로 옮긴다는 의미이다.
    else: # 원판 개수가 2개~20개 사이라면
        Hanoi(n-1, a, c, b) # n-1개의 원판을 두번째 기둥으로 옮긴다.
        Hanoi(1, a, b, c) # 첫번째 기둥에 남아있는 1개의 원판을 세번째 기둥으로 옮긴다.
        Hanoi(n-1, b, a, c) # 두번째 기둥에 옮겨놓았던 n-1개의 원판을 세번째 기둥으로 옮긴다.

n = int(input()) # 원반의 개수를 입력받는다.
print(2**n-1) # 하노이 탑을 완전히 옮기려면 원반을 몇 번 옮겨야하는지 출력한다.
Hanoi(n, 1, 2, 3) # 옮기는 순서를 출력한다. Ex) 1 3 으로 출력될 경우, 첫번째 탑의 제일 위에 있는 원반을 세번째 탑으로 옮긴다는 의미이다.