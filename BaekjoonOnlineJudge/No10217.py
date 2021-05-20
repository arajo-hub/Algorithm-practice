import sys

t = int(sys.stdin.readline())
INF = sys.maxsize

for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())

    ticket = [[] for _ in range(n+1)]

    for _ in range(k):
        u, v, c, d = map(int, sys.stdin.readline().split())
        ticket[u].append([v, c, d])

    dp = [[INF for _ in range(m+1)] for _ in range(n+1)]
    dp[1][0] = 0

    for c in range(m+1):
        for d in range(1, n+1):
            if dp[d][c] == INF: continue
            t = dp[d][c]
            for dv, dc, dd in ticket[d]:
                if dc + c > m:
                    continue
                dp[dv][dc+c] = min(dp[dv][dc+c], t+dd)
    
    result = min(dp[n])

    if result == INF:
        print('Poor KCM')
    else:
        print(result)