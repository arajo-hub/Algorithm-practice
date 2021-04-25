def solution(n, computers):
    answer = 0

    # 방문했는지 여부를 표시할 visited
    visited = [False for i in range(n)]

    # 컴퓨터 한 대씩 탐색
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            # dfs 한 번이 끝나고 나오면 그 컴퓨터와 연결된 모든 경로를 탐색한 것이므로 answer에 +1
            answer += 1
    return answer

def dfs(n, computers, com, visited):
    # 방문한 것으로 처리
    visited[com] = True

    # 컴퓨터 한 대씩 탐색
    for connect in range(n):
        # 그 자신이 아니면서 연결된 상태이고,
        if connect != com and computers[com][connect] == 1:
            # 방문한 적이 없으면
            if visited[connect] == False:
                # 그 컴퓨터에서 또 탐색
                dfs(n, computers, connect, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 답은 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 답은 1