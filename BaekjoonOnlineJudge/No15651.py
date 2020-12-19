# 문제
# 자연수 n과 m이 주어졌을 때,
# 아래 조건을 만족하는 길이가 m인 수열을 모두 구하는 프로그램을 작성하시오.

from itertools import combinations_with_replacement
import sys

n, m=map(int, sys.stdin.readline().split())
array=[]

def solution(depth, n, m):
    print(array)
    if depth==m:
        print(' '.join(map(str, array)))
        return
    for i in range(n):
        array.append(i+1)
        solution(depth+1, n, m)
        array.pop()
        
    
solution(0, n, m)