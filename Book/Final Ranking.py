from collections import deque
import sys

for tc in range(int(sys.stdin.readline())):
    n=int(sys.stdin.readline())
    indegree=[0]*(n+1)
    graph=[[False]*(n+1) for i in range(n+1)] # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬

    data=list(map(int, sys.stdin.readline().split())) # 작년 순위 정보 입력
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]]=True
            indegree[data[j]]+=1

    m=int(sys.stdin.readline()) # 올해 변경된 순위 정보 입력
    for i in range(m):
        a, b=map(int, sys.stdin.readline().split())
        # 방향을 뒤집어준다.
        if graph[a][b]:
            graph[a][b]=False
            graph[a][b]=True
            indegree[a]+=1
            indegree[b]-=1
        else:
            graph[a][b]=True
            graph[b][a]=False
            indegree[a]-=1
            indegree[b]+=1

    result=[]
    q=deque()

    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)

    certain=True
    cycle=False

    for i in range(n):
        if len(q)==0: # 큐가 비어 있다면 사이클이 발생했다는 의미
            cycle=True
            break

        if len(q)>=2: # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
            certain=False
            break

        now=q.popleft()
        result.append(now)
        for i in range(1, n+1):
            if graph[now][i]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)

    if cycle: # 사이클이 발생하는 경우(일관성이 없는 경우)
        print("IMPOSSIBLE")
    elif not certain: # 위상 정렬 결과가 여러 개인 경우
        print("?")
    else: # 위상 정렬을 수행한 결과를 출력한다.
        for i in result:
            print(i, end=' ')
        print()