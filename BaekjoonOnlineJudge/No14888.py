import sys

sys.setrecursionlimit(10**9)

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))

minimum = 10**9
maximum = -10**9

def dfs(now, level):
    if level == N:
        global minimum, maximum
        maximum = max(now, maximum)
        minimum = min(now, minimum)
        return
    
    if operator[0] > 0:
        operator[0] -= 1
        dfs(now + numList[level], level+1)
        operator[0] += 1
    
    if operator[1] > 0:
        operator[1] -= 1
        dfs(now - numList[level], level+1)
        operator[1] += 1
    
    if operator[2] > 0:
        operator[2] -= 1
        dfs(now * numList[level], level+1)
        operator[2] += 1
    
    if operator[3] > 0:
        result = abs(now) // numList[level]
        if now < 0:
            result *= -1
        
        operator[3] -= 1
        dfs(result, level+1)
        operator[3] += 1
        
now = numList[0]
dfs(now, 1)

sys.stdout.write(str(maximum) + "\n" + str(minimum) + "\n")