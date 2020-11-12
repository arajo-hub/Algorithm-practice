# import sys

# N, M=map(int, sys.stdin.readline().split()) # N은 볼링공의 개수, M은 공의 최대 무게

# bowlingball=list(map(int, sys.stdin.readline().split()))

# idx, cnt=0, 0
# for i in range(N):
#     idx=bowlingball[i]
#     for j in range(i+1, N):
#         if idx==bowlingball[j]:
#             pass
#         else:
#             cnt+=1

# print(cnt)

# # 다른 풀이방법

# array=[0]*11 # 1~10까지의 무게를 구분해서 담을 list


# for x in bowlingball: # bowlingball에서 차례로 무게(x)를 꺼내서
#     array[x]+=1 # 무게담는 list에 같은 무게의 공 개수를 세서 넣어준다.

# result=0
# for i in range(1, M+1):
#     N-=array[i] # 볼링공 개수에서 i무게의 공 개수를 빼준다.
#     result+=array[i]*N # result는 i무게의 공 개수 * 남은 공 개수를 더해준다.
#     # i무게의 공을 선택하면 그외의 공을 하나 선택하면 된다. 그런데 같은 무게여도 공을 구분한다고 되어있으므로
#     # i 무게의 공들 중 하나를 선택할 경우의 수(=i무게의 공 개수) * 남은 공들 중 하나를 선택할 경우의 수(=남은 공 개수)가 된다.

# print(result)

# 2020년 11월 12일 풀이

import sys

n, m=map(int, sys.stdin.readline().split())

ball=list(map(int, sys.stdin.readline().split()))

array=[0]*m # 무게에 따라 공들을 정리

for x in ball: # 각 무게에 따라 공 분류(리스트에는 개수 표시)
    array[x]+=1

result=0
for i in range(1, m+1):
    n-=array[i]
    result+=array[i]*n # i무게의 공들 중 하나를 선택할 경우의 수 * 남은 공들 중 하나를 선택할 경우의 수

print(result)