from collections import deque
import sys

k = int(sys.stdin.readline())

def bfs(start):

    bi[start] = 1
    q = deque()
    q.append(start)

    while q:

        a = q.popleft()

        # 제일 처음엔 start와 연결된 정점들 탐색
        # 이후로는 그 정점들과 연결된 정점들 계속 탐색
        for i in s[a]:
            if bi[i] == 0: # 연결된 정점이면
                bi[i] = -bi[a] # -1로 바꿔준다.
                q.append(i)
            else:
                if bi[i] == bi[a]:
                    return False
    return True

for i in range(k):

    v, e = map(int, input().split())

    isTrue = True

    s = [[] for i in range(v + 1)]
    bi = [0 for i in range(v + 1)]

    for j in range(e):
        a, b = map(int, input().split())
        # 그 칸의 인덱스를 정점으로, 연결된 노드들을 넣어준다.
        # 2번 정점이 1, 3, 4와 연결되어 있다고 하면
        # s[2] = [1, 3, 4] 이렇게.
        s[a].append(b)
        s[b].append(a)

    # 정점을 하나씩 탐색
    for k in range(1, v + 1):
        if bi[k] == 0: # 탐색하지 않은 곳이고,
            if not bfs(k):
                isTrue = False
                break

    print("YES"if isTrue else "NO")