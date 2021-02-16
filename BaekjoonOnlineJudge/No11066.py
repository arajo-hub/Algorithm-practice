import sys

t=int(sys.stdin.readline())

for __ in range(t):
    k = int(input()) # 소설을 구성하는 장의 수
    page = list(map(int, sys.stdin.readline().split())) # 각 장의 페이지 수
    
    table = [[0]*k for _ in range(k)]
    
    for i in range(k-1):
        table[i][i+1] = page[i] + page[i+1]
        for j in range(i+2, k):
            table[i][j] = table[i][j-1] + page[j]
    
    for d in range(2, k):
        for i in range(k-d):
            j = i+d
            minimum = [table[i][k] + table[k+1][j] for k in range(i, j)] 
            table[i][j] += min(minimum)
    
    print(table[0][k-1])

# 출처: https://suri78.tistory.com/15