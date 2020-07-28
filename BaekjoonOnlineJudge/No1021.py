n, m = map(int, input().split())
idx = list(map(int, input().split()))

step = 0


def move_left(que):
    global step
    step += 1

    tmp = que.pop(0)
    que.append(tmp) # 제일 앞에 있는 수를 제일 뒤로 가져온다.


def move_right(que):
    global step
    step += 1

    tmp = [que.pop(-1)]
    tmp.extend(que) # 제일 뒤에 있는 값을 앞으로 가져온다.
    que = tmp

    return que


# que 만들기
que = list(range(1, n + 1))

# 원하는 수를 다 뽑을 때까지 반복
while idx:
    if que[0] == idx[0]:
        que.pop(0)
        idx.pop(0)
    else:
        # 움직인다.
        if que.index(idx[0]) <= len(que) // 2: # 중간수보다 작으면 왼쪽으로 이동
            while que[0] != idx[0]: move_left(que)
        else: # 중간수보다 크면 오른쪽으로 이동
            while que[0] != idx[0]: que = move_right(que)

print(step)