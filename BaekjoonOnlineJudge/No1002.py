t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # d는 두 개 원의 중심 사이의 거리
    rs = r1 + r2
    rm = abs(r1 - r2)
    if d == 0: # 두 원의 중심이 같을 때(두 중심 사이의 거리가 0)
        if r1 == r2: # 반지름이 같다면 원은 겹친다.
            print(-1)
        else: # 반지름이 같지 않다면 아예 만나지 않는다.
            print(0)
    else: # 중심이 같지 않을 때(두 중심 사이의 거리가 있을 때)
        if d == rs or d == rm: # 두 개 원의 중심 사이의 거리가 반지름의 합 혹은 차이와 같다면
            print(1) # 접점은 1개
        elif d < rs and d > rm: # 반지름의 합보다 작거나 반지름의 차이보다 크다면
            print(2) # 접점은 2개
        else: # 그게 아니라면
            print(0) # 두 원의 접점은 없다.