from sys import stdin
read=stdin.readline
case=[]

def classavg(numList):
    avg=sum(numList[1:])/case[0]
    cnt=0
    for i in range(1, len(numList)):
        if numList[i]>avg:
            cnt+=1
    return (cnt/case[0])*100

for i in range(int(read())):
    case=list(map(int, read().split()))
    print("%.3f"%classavg(case)+'%')

# 위는 2020년 6월 25일에 새로 푼 코드.
# 메모리는 29380KB 시간은 64ms 코드길이 335B

# 아래는 2020년 1월 5일에 풀었던 코드.
# 메모리는 29284KB 시간은 64ms 코드길이 419B
# 5달 전에 푼 문제인데 아래 코드와 위 코드를 보면 정말 차이가 많이 난다.
# 아래는 정말 엉망진창... 효율성을 생각하지도 않고 이중for문도 쓰고.
# 매일 알고리즘문제를 하나씩 풀면서 과연 내 코드가 여러면에서 나아지고 있는걸까 생각했는데
# 아래의 코드를 보니 나아지고 있는 건 확실하다.

casecount=int(input())
cases=[]
aver=[]
sum=0
count=0

for i in range(casecount):
    cases.append(input().split())

for i in range(casecount):
    for j in cases[i][1:]:
        sum+=int(j)
    aver.append(sum/int(cases[i][0]))
    sum=0

for i in range(casecount):
    for j in cases[i][1:]:
        if int(j)>float(aver[i]):
            count+=1
    print('{:1.3f}%'.format((count/int(cases[i][0]))*100))
    count=0