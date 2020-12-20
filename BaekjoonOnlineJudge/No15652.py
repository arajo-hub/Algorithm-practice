from itertools import permutations
import sys

n, m=map(int, sys.stdin.readline().split())
array=[]

def solution(depth, n, m, index):
    if depth==m:
        print(' '.join(map(str, array)))
        return
    for i in range(index, n):
        array.append(i+1)
        solution(depth+1, n, m, i)
        array.pop()
        
    
solution(0, n, m, 0)