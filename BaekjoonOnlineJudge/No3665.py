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
            if i==change_b:
                tree[change_a].remove(change_b)
                tree[change_b].append(change_a)
                inDegree[change_b]-=1
                inDegree[change_a]+=1
                check=False
        if check:
            tree[change_b].remove(change_a)
            tree[change_a].append(change_b)
            inDegree[change_a] -= 1
            inDegree[change_b] += 1
 
 
    for i in range(1,n+1):
        if inDegree[i]==0:
            q.append(i)
 
    result=0
    result_list=[]
    if not q:
        result=1
    while q:
        if len(q)>1:
            result=1
            break
        a=q.popleft()
        result_list.append(a)
        for i in tree[a]:
            inDegree[i]-=1
            if inDegree[i]==0:
                q.append(i)
            elif inDegree[i]<0:
                result=1
                break
 
    if result>0 or len(result_list)<n:
        print('IMPOSSIBLE')
    else:
        print(*result_list)

# 출처 : https://developmentdiary.tistory.com/464