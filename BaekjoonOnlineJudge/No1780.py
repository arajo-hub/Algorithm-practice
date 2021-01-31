import sys

n=int(sys.stdin.readline()) # 종이의 크기

paper=[]
temp=[]
for i in range(n):
    temp=list(map(int, sys.stdin.readline().split()))
    paper.append(temp)

minus_count=0
zero_count=0
one_count=0

def solution(array, start_x, start_y, length):
    global minus_count
    global zero_count
    global one_count

    previous=array[start_x][start_y]
    isMixed=False
    for i in range(start_x, start_x+length):
        for j in range(start_y, start_y+length):
            if previous!=array[i][j]:
                isMixed=True
                break
        if (isMixed):
            break
    
    if (isMixed): # 여러 수들로 구성되어 있다면
        # 9개로 자른 종이를 다시 확인
        # 왼쪽 위 0,0 ~ 2,2
        solution(array, start_x, start_y, length//3)
        # 가운데 위 0,3 ~ 2,5
        solution(array, start_x, start_y+length//3, length//3)
        # 오른쪽 위 0,6 ~ 2,8
        solution(array, start_x, start_y+(length//3)*2, length//3)
        # 왼쪽 중간 3,0 ~ 5, 2
        solution(array, start_x+length//3, start_y, length//3)
        # 가운데 중간 3,3 ~ 5,5
        solution(array, start_x+length//3, start_y+length//3, length//3)
        # 오른쪽 중간 3,6 ~ 5,8
        solution(array, start_x+length//3, start_y+(length//3)*2, length//3)
        # 왼쪽 아래 6,0 ~ 8,2
        solution(array, start_x+(length//3)*2, start_y, length//3)
        # 가운데 아래 6,3 ~ 8,5
        solution(array, start_x+(length//3)*2, start_y+length//3, length//3)
        # 오른쪽 아래 6,6 ~ 8,8
        solution(array, start_x+(length//3)*2, start_y+(length//3)*2, length//3)
    else:
        if array[start_x][start_y]==-1:
            minus_count+=1
        elif array[start_x][start_y]==0:
            zero_count+=1
        elif array[start_x][start_y]==1:
            one_count+=1

solution(paper, 0, 0, len(paper))
print(minus_count)
print(zero_count)
print(one_count)

# solution 안의
# for i in range(start_x, start_x+length):
#         for j in range(start_y, start_y+length):
#             if previous!=array[i][j]:
#                 isMixed=True
#                 break
#         if (isMixed):
#             break
# 에서 처음에 굳이 안해도 되겠지 싶어서 break문 없이 돌렸는데 시간초과.
# 그래서 break문으로 경우의 수를 줄여주니 통과했다.