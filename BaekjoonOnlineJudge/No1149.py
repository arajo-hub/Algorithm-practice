import sys

N=int(sys.stdin.readline())
costlist=[]
min_idx=0
cost=0

for i in range(N):
    costlist.append(list(map(int, sys.stdin.readline().split())))

for j in range(N):
    if j==0:
        cost+=min(costlist[j])
        min_idx=costlist[j].index(min(costlist[j]))
    else:
        costlist[j][min_idx]=1000
        cost+=min(costlist[j])
        min_idx=costlist[j].index(min(costlist[j]))

print(cost)

# 위 코드는 내가 풀어본 코드.
# 첫 집에서 가장 적은 비용이 드는 색을 고르고, 그 색의 인덱스를 기억해뒀다가
# 다음집으로 가면 기억해뒀던 인덱스의 값은 1000으로 가장 높게 해놓고
# 그집의 최솟값을 구하는 방법인데(결국 전집에서 고른 색의 인덱스는 제외하는 셈)
# 백준에서는 틀렸다고 하는데 왜 틀렸는지 모르겠다.

# 아래는 구글에서 찾아본 코드.
# 출처는 https://inspirit941.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-1149-RGB%EA%B1%B0%EB%A6%AC

import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
table = [[0 for _ in range(3)] for _ in range(n)] # table로 구현하고
for i in range(n):
    for j in range(3):
        if i == 0:
            table[i][j] = arr[i][j] # 첫번째 집의 경우는 table에 첫번째 집의 색깔별 비용을 그대로 넣어준다.
        else: # 첫번째 이후의 경우,
            table[i][j] = min(table[i-1][(j+1)%3], table[i-1][(j+2)%3]) + arr[i][j] #전집에서 선택한 색깔을 제외하고, 나머지 두 색 중 비용이 적게 드는 색과 지금 집의 색을 더한다.
print(min(table[-1])) # 위와 같은 연산을 반복하여 만들어지는 table의 제일 마지막 칸에는 모든 경우의 총비용이 있다. 그 중에 가장 작은 값을 구하면 된다.