import sys

# 모두 0 -> 압축결과 0
# 모두 1 -> 압축결과 1
# 0, 1 섞여있으면 -> 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 4개로 나눠서 압축

# 8*8이면
# 왼위는 0, 0 ~ 3, 3
# 오위는 0, 4 ~ 3, 7
# 왼아는 4, 0 ~ 7, 3
# 오아는 4, 4 ~ 7, 7

n=int(sys.stdin.readline()) # 영상의 크기
result=""
video=[]
temp=[] # video의 한 행을 담아줄 배열
for i in range(n):
    temp.extend(sys.stdin.readline().strip('\n'))
    video.append(temp)
    temp=[]

def solution(array, start_x, start_y, length):
    global result
    before=array[start_x][start_y]
    isMixed=False
    for i in range(start_x, start_x+length+1):
        for j in range(start_y, start_y+length+1):
            if before!=array[i][j]:
                isMixed=True
                break
    
    if (isMixed):
        result+="("
        # 0, 1 섞여있으므로 네 방향을 검사
        solution(array, start_x, start_y, length//2) # 왼쪽 위
        solution(array, start_x, start_y+length//2+1, length//2) # 오른쪽 위
        solution(array, start_x+length//2+1, start_y, length//2) # 왼쪽 아래
        solution(array, start_x+length//2+1, start_y+length//2+1, length//2) # 오른쪽 아래
        result+=")"
    else: # 섞여있지 않은 경우
        result+=array[start_x][start_y]
    

solution(video, 0, 0, len(video)-1)
print(result)