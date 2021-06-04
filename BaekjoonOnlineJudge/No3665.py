import sys
from collections import deque
 
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    ranking=list(map(int,sys.stdin.readline().split()))
    tree=[[] for _ in range(n+1)]
    inDegree=[0 for _ in range(n+1)]
    q=deque()
    for i in range(0,n-1):
        for j in range(i+1,n):
            tree[ranking[i]].append(ranking[j])
            inDegree[ranking[j]]+=1
 
 
    m=int(sys.stdin.readline())
    for _ in range(m):
        change_a,change_b=map(int,sys.stdin.readline().split())
        check=True
        for i in tree[change_a]:
            if i==change_b:#change_a가 더 높은 순위 의 팀일때
                tree[change_a].remove(change_b)
                tree[change_b].append(change_a)
                inDegree[change_b]-=1
                inDegree[change_a]+=1
                check=False
        if check:#change_b가 더 높은 순위 의 팀일때
            tree[change_b].remove(change_a)
            tree[change_a].append(change_b)
            inDegree[change_a] -= 1
            inDegree[change_b] += 1
 
 
    for i in range(1,n+1):#진입차수 0인거 찾기
        if inDegree[i]==0:
            q.append(i)
 
    result=0  #0가능 1불가
    result_list=[]
    if not q:#진입차수가 처음부터 0이 없을때
        result=1
    while q:
        if len(q)>1:#두개이상 들어왔을때
            result=1
            break
        a=q.popleft()
        result_list.append(a)
        for i in tree[a]:
            inDegree[i]-=1
            if inDegree[i]==0:
                q.append(i)
            elif inDegree[i]<0:#사이클이 있을때
                result=1
                break
 
    if result>0 or len(result_list)<n:
        print('IMPOSSIBLE')
    else:
        print(*result_list)