import sys

def solution(priorities, location):
    answer=0
    while(len(priorities)!=0):
        if location==0:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location=len(priorities)-1
            else:
                return answer+1
        else:
            if priorities[0]<max(priorities):
                priorities.append(priorities.pop(0))
                location-=1
            else:
                priorities.pop(0)
                location-=1
                answer+=1
    return answer

testcase=int(sys.stdin.readline())
importance=[]
answer=0

for i in range(testcase):
    doct_count, doct_indx=map(int, sys.stdin.readline().split())
    importance=list(map(int, sys.stdin.readline().split()))
    print(solution(importance, doct_indx))