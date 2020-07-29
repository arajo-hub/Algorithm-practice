numlist=[]

for i in range(int(input())):
    numlist.append(int(input()))

for i in range(len(numlist)):
    for j in range(i+1, len(numlist)):
        if numlist[i]>numlist[j]:
            numlist[i], numlist[j]=numlist[j], numlist[i]

for k in numlist:
    print(k)