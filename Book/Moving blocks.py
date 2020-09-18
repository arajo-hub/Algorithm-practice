from collections import deque

def get_next_pos(pos, board): # pos에서 갈 수 있는 새 위치를 찾는다.
    next_pos=[]
    pos=list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y=pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    for i in range(4): # 4방향을 검토
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y=pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        if board[pos1_next_x][pos1_next_y]==0 and board[pos2_next_x][pos2_next_y]==0: # board에서 새 위치가 벽이 아니라면
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)}) # 다음 위치에 추가한다.
    if pos1_x==pos2_x: # 로봇이 가로로 놓여있다면
        for i in [-1, 1]:
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0: # 위쪽으로 회전하거나, 아래쪽으로 회전해도 벽이 아니라면
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})   # 그 위치를 다음 위치에 추가한다.
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    elif pos1_y==pos2_y: # 로봇이 세로로 놓여있다면
        for i in [-1, 1]:
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0: # 왼쪽으로 회전하거나, 오른쪽으로 회전해도 벽이 아니라면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})   # 그 위치를 다음 위치에 추가한다.
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    return next_pos

def solution(board):
    n=len(board)
    new_board=[[1]*(n+2) for _ in range(n+2)] # 로봇이 이동할 지도를 만든다.
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j] # 입력한 board를 new_board에 옮긴다.
    q=deque()
    visited=[]
    pos={(1, 1), (1, 2)} # 로봇의 위치
    q.append((pos, 0))
    visited.append(pos) # 방문한 곳으로 넣어놓는다.
    while q:
        pos, cost=q.popleft() # q에서 로봇의 위치와 시간을 꺼낸다.
        if (n, n) in pos: #(n, n)에 로봇에 있으면 끝난다.
            return cost
        for next_pos in get_next_pos(pos, new_board): # 현재 위치에서 새 위치를 찾아서
            if next_pos not in visited: # 방문하지 않은 곳이라면
                q.append((next_pos, cost+1)) # q에 넣어주고
                visited.append((next_pos)) # 방문한 곳으로 처리한다.
    return 0