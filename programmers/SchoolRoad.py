def solution(m, n, puddles):
    maps=[[0]*(m+1) for _ in range(n+1)]
    maps[1][1]=1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [j, i] in puddles:
                maps[i][j]=0
            else:
                maps[i][j]+=(maps[i-1][j]+maps[i][j-1])
    return (maps[-1][-1])%1000000007

# 코드 출처는 https://post.naver.com/viewer/postView.nhn?volumeNo=26933342&memberNo=33264526
# 이 문제의 관건은 [a, b]=[a-1, b]+[a, b-1]이라는 것