def bfs(n):

    second = 0
    q = deque([[n, second]])

    while q:
        popped = q.popleft()

        num = popped[0]
        second = popped[1]

        # 방문한 적이 없는 수일 때
        if not visited[num]:
            visited[num] = True

            # 동생의 위치와 같으면 second 리턴
            if num == k:
                return second
            
            # 동생의 위치와 같지 않으면 second를 1 올려주고
            # 큐에 자식노드들을 채운다.
            second+=1
            if (num*2) <= 100000:
                q.append([num*2, second])
            if (num+1) <= 100000:
                q.append([num+1, second])
            if (num-1) >= 0:
                q.append([num-1, second])
    
    return second


from collections import deque
import sys

# 수빈이의 위치 n, 동생의 위치 k
n, k = map(int, sys.stdin.readline().split())

visited = [False] * 100001
print(bfs(n))