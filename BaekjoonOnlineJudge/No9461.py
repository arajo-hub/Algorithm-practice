import sys

def solution(case):
    numList=[0]*(case+1)
    if case<=2:
        return 1
    else:
        numList[1], numList[2], numList[3] = 1, 1, 1
        for j in range(3, case+1):
            numList[j]=numList[j-3]+numList[j-2]
        return numList[-1]

for i in range(int(sys.stdin.readline())):
    case=int(sys.stdin.readline())
    print(solution(case))