from collections import deque
import sys
import copy

N=int(sys.stdin.readline())
indegree=[0]*(N+1)
graph=[[] for i in range(N+1)]
time=[0]*(N+1)

for i in range(1, N+1):
    data=list(map(int, sys.stdin.readline().split())) # data는 시간, 들어야 할 과목 번호, 과목 번호, ... , -1로 이루어진다.
    time[i]=data[0] # data의 제일 앞에 오는 시간은 따로 time리스트에 저장하고,
    for x in data[1:-1]: # 그 다음의 data들(들어야 할 과목번호들)은 graph에 저장한다.
        indegree[i]+=1
        graph[x].append(i)
        print(indegree)
        print(graph)

def topology_sort():
    result=copy.deepcopy(time)
    q=deque()

    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now=q.popleft()
        for i in graph[now]:
            result[i]=max(result[i], result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in range(1, N+1):
        print(result[i])

topology_sort()