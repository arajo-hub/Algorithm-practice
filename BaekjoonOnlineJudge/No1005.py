import sys
from collections import deque
 
 # 테스트케이스의 개수
T=int(sys.stdin.readline())

for _ in range(T):
    # 건물의 개수 N, 건물간의 건설순서규칙의 개수 K
    N, K=map(int,sys.stdin.readline().split())

    # 각 건물당 건설에 걸리는 시간이 공백을 사이로 주어짐
    building = [0] + list(map(int,sys.stdin.readline().split()))
    # 건설순서
    tree=[[] for _ in range(N+1)]
    # 진입차수
    inDegree=[0 for _ in range(N+1)]
    DP=[0 for _ in range(N+1)]

    for _ in range(K):#건설규칙 저장
        a, b = map(int,sys.stdin.readline().split())
        tree[a].append(b)
        inDegree[b] += 1
 
    q = deque()
    for i in range(1, N+1):
        if inDegree[i] == 0: # 진입차수가 0이라면 큐에 넣는다.
            q.append(i)
            DP[i] = building[i]
 
    while q:
        a = q.popleft()
        for i in tree[a]:
            inDegree[i] -= 1
            DP[i] = max(DP[a] + building[i],DP[i])
            if inDegree[i] == 0:
                q.append(i)
 
 
    answer=int(sys.stdin.readline())
    print(DP[answer])