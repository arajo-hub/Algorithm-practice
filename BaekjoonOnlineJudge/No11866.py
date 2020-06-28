import sys

N, K=map(int, sys.stdin.readline().split())
stack = []
idx=0
people=[i for i in range(1, N+1)]
while (len(people)!=0):
    idx += (K - 1)
    if idx >= len(people):
        idx = idx % len(people)
    stack.append(people.pop(idx))

print('<', end='')
print(*stack, sep=', ', end='')
print('>')