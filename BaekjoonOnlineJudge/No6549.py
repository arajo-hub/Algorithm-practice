import sys

while(True):
    
    n, *square=list(map(int, sys.stdin.readline().split()))
    # 이런 식으로도 입력받을 수 있다는 것 알아두기!

    if n==0:
        break

    square.insert(0, 0) # 맨 앞자리(index 0)에 0 넣어주고,
    square+=[0] # 끝에도 0 추가

    checked=[0]
    answer=0

    for i in range(1, n+2):
        while(checked and (square[checked[-1]]>square[i])):
            # 현재 높이보다 이전 높이가 높을 때 높이 구하기 시작 (이제 내려가기 시작)
            height=checked.pop() # 이전 높이 뽑아서
            answer=max(answer, (i-1-checked[-1])*square[height]) # 이전 높이의 위치부터 현재까지의 거리*이전 높이 -> 히스토그램에서 구할 수 있는 그 높이의 직사각형!
        # 현재 높이보다 이전 높이가 낮거나 같을 때는 checked에 추가만.(올라가는 중)
        checked.append(i)
    print(answer)