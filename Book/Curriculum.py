from collections import deque
import sys
import copy

N=int(sys.stdin.readline())
indegree=[0]*(N+1)
graph=[[] for i in range(N+1)]
time=[0]*(N+1)

for i in range(1, N+1): # i는 과목번호.
    data=list(map(int, sys.stdin.readline().split())) # data는 시간, 들어야 할 과목 번호, 과목 번호, ... , -1로 이루어진다.
    time[i]=data[0] # data의 제일 앞에 오는 시간은 따로 time리스트에 저장하고,
    for x in data[1:-1]: # data[1:-1]은 선수과목 번호가 나열된 리스트. 즉, x는 선수과목 번호를 의미.
        indegree[i]+=1 # i가 1이면 indegree[1]+=1인데, 이 의미는 1번 과목을 들으려면 선수과목을 1개 더 들어야 한다는 의미. 즉, indegree는 선수과목의 개수.
        graph[x].append(i) # graph는 어떤 과목(x)을 들은 후에 몇 번의(순서적 의미) 과목을 들어야 하는지 의미. graph[2].append(1)이라면 2번 과목을 듣고 1번 과목을 들어야 함을 의미.

def topology_sort():
    result=copy.deepcopy(time) # deepcopy는 내부의 객체들까지 모두 copy. a를 deepcopy한 b가 있을 때, a 내부 객체에 변화를 주어도 b는 본래 카피된 a의 형태.
    q=deque()

    for i in range(1, N+1): # i는 과목번호.
        if indegree[i]==0: # 들어야 할 선수과목이 없다면
            q.append(i) # q에 과목번호를 넣어준다.

    while q:
        now=q.popleft() # 선수과목이 없는 과목번호를 꺼낸다.
        for i in graph[now]: # i는 선수과목이 없는 과목을 들은 후, 다음으로 들어야 하는 과목을 의미. graph는 index과목 이후에 들어야 할 과목을 나타내므로.
            result[i]=max(result[i], result[now]+time[i]) # i과목을 듣는 시간은 결과적으로 1. result[i]와 2. 선수과목이 없는 과목을 듣는 시간과 i과목을 듣는 시간을 합친 값 중 최대값.
            indegree[i]-=1 # 위의 과정을 거치며 선수과목(now)을 하나 들은 셈이 되므로 -1을 해준다.
            if indegree[i]==0: # 들어야 할 선수과목이 없다면
                q.append(i) # q에 과목번호를 넣어준다.

    for i in range(1, N+1):
        print(result[i])

topology_sort()