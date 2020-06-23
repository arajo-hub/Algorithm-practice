import sys

n = int(sys.stdin.readline())

coloredPaper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 색종이 전체를 입력한다.

white, blue = 0, 0

def divide(x, y, n):
    global blue, white
    point = coloredPaper[x][y] # 시작점을 잡아준다.
    for i in range(x, x + n): # 시작점과 시작점으로부터 n만큼 떨어져있는 거리 안의 색종이들중에
        for j in range(y, y + n): # y도 위의 x과 같이 시작점과 시작점으로부터 n만큼 떨어져있는 거리의 범위를 잡았으므로 n만큼의 정사각형의 색종이들 중에
            if point != coloredPaper[i][j]: # 하나라도 시작점과 다르다면(=색상이 다른 색종이가 하나라도 있다면)
                # 네 영역으로 나눈다.
                divide(x, y, n // 2)
                divide(x, y + n // 2, n // 2)
                divide(x + n // 2, y, n // 2)
                divide(x + n // 2, y + n // 2, n // 2)
                return

    if point == 0:  # 모두 흰색이라면
        white += 1
        return
    else:  # 모두 파란색이라면
        blue += 1
        return


divide(0, 0, n)
print(white)
print(blue)

# 위 코드는 코드 길이 1197 B, 시간 80 ms, 메모리 29380 KB가 소요.
# 아래는 백준 채점 현황 중 numna님의 코드. (코드 길이 491 B, 시간 100 ms, 메모리 29516 KB)

def go(x, y, n):
    is_one = 1
    for i in range(y, y + n):
        for j in range(x, x + n):
            if data[y][x] != data[i][j]:
                is_one = 0
    if is_one:
        ans.append(data[y][x])
    else:
        n //= 2
        go(x, y, n)
        go(x + n, y, n)
        go(x, y + n, n)
        go(x + n, y + n, n)


n = int(input())
data = [[int(i) for i in input().strip().split()]
        for _ in range(n)]

ans = []
go(0, 0, n)

print(ans.count(0))
print(ans.count(1))