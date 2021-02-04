def solution(a, b):

    # 1제곱이라면
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000 # 그냥 각 요소를 1000으로 나눠서 출력
        return a

    # 홀수제곱이라면
    elif b % 2 > 0:
        # 계산할 값을 저장할 임시 행렬 temp
        temp = [[0 for _ in range(n)] for _ in range(n)]
        
        # 홀수제곱이므로 2로 나눠지는 짝수제곱을 먼저 구해주고, 행렬을 한 번 더 곱한다.
        # ex) 구해야할 게 5제곱이라면, 2제곱을 먼저하고, 2제곱한 결과를 곱해서 4제곱을 만들고, 거기에 행렬을 한 번 더 곱하면 5제곱이 된다.
        c = solution(a, b-1) # b-1제곱한 결과
        
        # b-1제곱한 결과에 행렬을 한 번 더 곱해서 b제곱한 결과를 만들어준다.
        for i in range(n):
            for j in range(n):
                for t in range(n):
                    temp[i][j] += c[i][t] * a[t][j]
                temp[i][j] %= 1000
        return temp

    # 짝수제곱이라면
    else:
        temp = [[0 for _ in range(n)] for _ in range(n)]
        
        # 그 수를 반 나눈 제곱을 먼저 해준다.
        c = solution(a, b//2)

        # 반 나눴으므로 똑같은 결과로 두 번 곱한다.
        for i in range(n):
            for j in range(n):
                for t in range(n):
                    temp[i][j] += c[i][t] * c[t][j]
                temp[i][j] %= 1000
        return temp

n, b = map(int,input().split()) # 행렬의 크기 n과 몇 제곱인지를 나타내는 b

a = []
for _ in range(n):
    a.append(list((map(int, input().split()))))

for i in solution(a, b):
    for j in i:
        print(j, end = ' ')
    print()

https://hon6036.github.io/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5/10830/