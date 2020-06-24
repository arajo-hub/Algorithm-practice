from sys import stdin
read=stdin.readline # 변수 입력받을 때 꼭 sys.stdin.readline() <- 이렇게 안쓰고 본문과 같은 방법으로도 할 수 있다는 것 알아두고 활용하기.

dict={}

for i in range(int(read())): # 사전형을 만들어준다.
    dict[i+1]=set()

for j in range(int(read())): # 연결되어있는 컴퓨터 쌍을 사전형에 넣어준다. 이때 range는 연결되어있는 컴퓨터 쌍의 수.
    a, b=map(int, read().split())
    dict[a].add(b) # 예를 들자면, dict[1]={2, 3} 이라면 1번 컴퓨터와 연결된 컴퓨터는 2, 3번이다.
    dict[b].add(a)

def dfs(start, dict):
    for k in dict[start]: # dict[start]에서 시작해서 start번 컴퓨터와 연결된 컴퓨터들을 확인한다.
        if k not in visited: # 이미 방문했던 컴퓨터에 없다면
            visited.append(k) # visited에 추가해주고
            dfs(k, dict) # dfs를 반복한다.

visited=[]
dfs(1, dict)
print(len(visited)-1)

# 코드 출처 : https://chancoding.tistory.com/60
# 후에 BFS 추가 예정