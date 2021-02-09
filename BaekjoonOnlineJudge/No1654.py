import sys

k, n=map(int, sys.stdin.readline().split())

line=[int(sys.stdin.readline()) for _ in range(k)]
start=1
end=max(line)

while(start<=end):
    std=(start+end)//2
    count=0
    for i in range(len(line)):
        count+=line[i]//std
    if count>=n:
        start=std+1
    else:
        end=std-1

print(end)