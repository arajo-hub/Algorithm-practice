import sys
input = sys.stdin.readline

def find(x, parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents, ranks):
    xroot = find(x, parents)
    yroot = find(y, parents)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def solution(n, m):
    parents = [i for i in range(n)]
    ranks = [0 for i in range(n)]
    result = 0
    found = False
    for i in range(1, m+1):
        a, b = map(int, input().split())
        if found: continue
        if find(a, parents) == find(b, parents):
            result = i
            found = True
        else:
            union(a, b, parents, ranks)
    print(result)

if __name__ == '__main__':
    solution(*map(int, input().split()))

# 출처 : https://yongjoonseo.dev/problem%20solving/PS-baekjoon026/