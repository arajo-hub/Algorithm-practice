import sys

N, M=map(int, sys.stdin.readline().split()) # N은 볼링공의 개수, M은 공의 최대 무게

bowlingball=list(map(int, sys.stdin.readline().split()))

idx, cnt=0, 0
for i in range(N):
    idx=bowlingball[i]
    for j in range(i+1, N):
        if idx==bowlingball[j]:
            pass
        else:
            cnt+=1

print(cnt)

array=[0]*11 # 1~10까지의 무게를 구분해서 담을 list

# 다른 풀이방법
for x in bowlingball: # bowlingball에서 차례로 무게(x)를 꺼내서
    array[x]+=1 # 무게담는 list에 같은 무게의 공 개수를 세서 넣어준다.

result=0
for i in range(1, M+1):
    N-=array[i] # 볼링공 개수에서 i무게의 공 개수를 빼준다.
    result+=array[i]*N # result는 i무게의 공 개수 * 남은 공 개수를 더해준다.
    # i무게의 공을 선택하면 그외의 공을 하나 선택하면 된다. 그런데 같은 무게여도 공을 구분한다고 되어있으므로
    # i 무게의 공들 중 하나를 선택할 경우의 수(=i무게의 공 개수) * 남은 공들 중 하나를 선택할 경우의 수(=남은 공 개수)가 된다.

print(result)