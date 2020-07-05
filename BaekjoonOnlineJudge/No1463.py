import sys

X=int(sys.stdin.readline())
cnt=0
minimum=[X]

def cal(numList):
    list=[]
    for i in numList:
        list.append(i-1) # -1 연산은 여기에서 해준다.
        if i%3==0:
            list.append(i/3) # i가 3으로 나누어지면 3으로 나눈 값을 추가하고,
        if i%2==0:
            list.append(i/2) # 2로 나누어지면 2로 나눈 값을 추가한다.
    return list

while True:
    if X==1:
        print(cnt)
        break
    temp=minimum[:]
    minimum=[]
    minimum=cal(temp)
    cnt+=1
    if min(minimum)==1:
        print(cnt)
        break

# 코드 출처는 https://doorbw.tistory.com/57