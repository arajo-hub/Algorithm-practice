import sys
 
T=sys.stdin.readline().replace("\n","")#문자열
P=sys.stdin.readline().replace("\n","")#패턴
 
KMPTable=[0 for _ in range(len(P))]
def MakeTable(P,KMPTable):
    j=0
    for i in range(1,len(P)):
        while j>0 and P[i]!=P[j]:#같지않을때
            j=KMPTable[j-1]#이전의 맞은부분곳까지 돌아가서 다시비교
        if P[i]==P[j]:#같을시
            j+=1#j를 증가시키고
            KMPTable[i]=j#테이블 갱신
 
def KMP(T,P,KMPTable):
    MakeTable(P, KMPTable)
    j=0
    count=0
    result=[]
    P_size=len(P)
    for i in range(len(T)):
        while j>0 and T[i]!=P[j]:#같지않을때
            j=KMPTable[j-1]#이전의 맞은부분곳까지 돌아가서 다시비교
        if T[i]==P[j]:#같으면
            if j==P_size-1:
                count+=1#개수 추가
                result.append(i-P_size+2)#위치추가
                j=KMPTable[j]#위치를 옮겨주고 다시탐색
            else:#j를 늘려준다
                j+=1
    return count,result

# 출처 : https://developmentdiary.tistory.com/455