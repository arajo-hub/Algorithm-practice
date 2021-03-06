import sys
from collections import deque
queue=deque()

for i in range(int(sys.stdin.readline())):
    cmd=list(sys.stdin.readline().split())
    if cmd[0]=='push_front':
        queue.insert(0, int(cmd[1]))
    elif cmd[0] == 'push_back':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd[0]=='pop_back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop())
    elif cmd[0]=='size':
        print(len(queue))
    elif cmd[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])