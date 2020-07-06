def solution(N):
    tiles=[1, 1]+[0]*(N-2)
    if N>2:
        for i in range(2, len(tiles)):
            tiles[i]=tiles[i-1]+tiles[i-2]
    else:
        if N==1:
            return 4
    return 4*tiles[-1]+tiles[-2]*2

print(solution(int(input())))