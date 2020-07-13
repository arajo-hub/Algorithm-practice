n, m = map(int, input().split())

check = [False] * (n + 1) # 중복으로 사용되는지 여부를 체크하는 리스트를 만들어준다.
a = [0] * m # m자리 수열을 만드는 용도


def go(index, n, m):
    if index == m: # m자리 수열을 다 채웠다면
        for i in range(m):
            print(a[i], end=' ') # 수열 출력
        print()
        return

    for i in range(1, n + 1): # 1부터 n+1까지
        if check[i]: # 만약 i가 이미 사용되었다면
            continue # i를 바꿔준다.
        check[i] = True # i가 아직 사용되지 않았다면 사용됨(True)로 바꿔주고,
        a[index] = i # m자리 수열을 만드는 용도인 a에 index자리에 i를 넣는다.
        go(index + 1, n, m) # m자리 수열 중 index를 채우고 그 다음 index자리를 채운다.
        check[i] = False

go(0, n, m)

# 코드 출처는 https://conak-diary.tistory.com/34