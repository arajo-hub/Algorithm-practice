import sys

n=int(sys.stdin.readline())

result=[]

num=2
while(n>1):
    if n%num==0: # num으로 나눠지면
        n//=num # 나누고
        result.append(num) # 나눈 수를 넣고
    else: # 나눠지지 않으면
        num+=1 # num을 1 올린다.

for i in result:
    print(i)