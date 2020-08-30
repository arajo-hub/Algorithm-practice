import sys

S=sys.stdin.readline().strip('\n')
result=0

count0, count1=0, 0

if S[0]=='1':
    count0+=1
else:
    count1+=1

for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        if S[i+1]=='1':
            count0+=1
        else:
            count1+=1

print(min(count0, count1))