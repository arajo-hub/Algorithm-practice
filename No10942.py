# 팰린드롬(palindrome)
# 앞에서부터 읽으나 뒤에서부터 읽으나 같은 단어

import sys

# 수열의 크기
n = int(sys.stdin.readline())

dp = [[0] * n for i in range(n)]
# 좌표값인 x, y가 수열의 x번째부터 y번째까지를 의미.
# x번째부터 y번째까지가 팰린드롬이라면 1로 표시

# 수열 만들기
num_list = list(map(int, sys.stdin.readline().split()))

for j in range(n):
    for start in range(n):
        end = start + j
        # j     0일 때
        # start 0 1 2 3 4 5 6 (n=7)
        # end   0 1 2 3 4 5 6

        # j     1일 때
        # start 0 1 2 3 4 5 6 (n=7)
        # end   1 2 3 4 5 6 7

        # j     2일 때
        # start 0 1 2 3 4 5 6 (n=7)
        # end   2 3 4 5 6 7 8

        # 결국 end의 시작값이 j라고 생각하면 된다.

        # 팰린드롬이 발생할 수 있는 경우의 수는 세 가지
        # 1. 숫자 1개의 경우(start, end가 같을 경우)
        # 2. 숫자 2개가 연달아있는 경우(start+1이 end인 경우)
        # 3. 숫자 3개 이상인 경우(start와 end 사이에 숫자(들)이 있는 경우)

        if end >= n: # end가 범위를 벗어나므로 종료
            break
        if start == end: # start와 end가 같으면 팰린드롬을 판별할 의미가 없으므로 dp에 1로 바꾸고 끝
            dp[start][end] = 1
            continue
        if start + 1 == end: # start와 end가 바로 연달아있고
            if num_list[start] == num_list[end]: # 수열에서 그 두 위치의 숫자가 같다면 팰린드롬
                dp[start][end] = 1
            continue
        if num_list[start] == num_list[end] and dp[start + 1][end - 1]: # 수열에서 start와 end의 위치에 있는 숫자가 같고, start+1부터 end-1까지의 수열(start와 end 내부의 수열)이 팰린드롬이라면 역시 팰린드롬
            dp[start][end] = 1

# 질문의 개수
m = int(sys.stdin.readline())

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s - 1][e - 1])