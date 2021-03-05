import sys

def solution(weight, weight_count, now, left, right, possible):
    new=abs(left-right)
    if (new not in possible):
        possible.append(new)
    if (now==weight_count):
        return 0
    if (result[now][new]==0):
        solution(weight, weight_count, now+1, left+weight[now], right, possible)
        solution(weight, weight_count, now+1, left, right+weight[now], possible)
        solution(weight, weight_count, now+1, left, right, possible)
        result[now][new]=1


weight_count=int(sys.stdin.readline()) # 추의 개수

weight=list(map(int, sys.stdin.readline().split()))

bead_count=int(sys.stdin.readline())

bead=list(map(int, sys.stdin.readline().split()))

possible=[]
result=[[0]*15001 for i in range(weight_count+1)]

solution(weight, weight_count, 0, 0, 0, possible)

for i in range(0, len(bead)):
    if (bead[i] in possible):
        print("Y", end=" ")
    else:
        print("N", end=" ")